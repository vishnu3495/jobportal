from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,FormView
from  candidate.forms import CandidateProfileForm,CandidateProfileUpdateForm
from candidate.models import CandidateProfile
from django.urls import reverse_lazy
from employer.models import User

class CandidateHomeView(TemplateView):
    template_name = "can-home.html"

class CandidateProfileView(CreateView):
    model = CandidateProfile
    form_class = CandidateProfileForm
    template_name = "candidates/can-profile.html"
    success_url = reverse_lazy("cand-home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class CandidateProfileDetailView(TemplateView):
    template_name = "candidates/can-profdetail.html"

class CandidateProfileEditView(FormView):
    model=CandidateProfile
    template_name = 'candidates/cand-editprof.html'
    form_class = CandidateProfileUpdateForm

    def get(self,request,*args,**kwargs):
        profile=CandidateProfile.objects.get(user=request.user)
        form=CandidateProfileUpdateForm(instance=profile,initial={
            "first_name":request.user.first_name,
            "last_name":request.user.last_name,
            "phone":request.user.phone,
            "email":request.user.email
            })
        return render(request,self.template_name,{"form":form})

    def post(self,request,*args,**kwargs):
        profile = CandidateProfile.objects.get(user=request.user)
        form=self.form_class(instance=profile,data=request.POST,files=request.FILES)
        if form.is_valid():
            first_name=form.cleaned_data.pop('first_name')
            last_name=form.cleaned_data.pop('last_name')
            phone=form.cleaned_data.pop('phone')
            email=form.cleaned_data.pop('email')
            form.save()
            user=User.objects.get(id=request.user.id)
            user.first_name=first_name
            user.last_name=last_name
            user.phone=phone
            user.email=email
            user.save()
            return redirect("cand-home")
        else:
            return render(request,self.template_name,{"form":form})



