from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DeleteView,UpdateView,DetailView,TemplateView,FormView
from employer.forms import JobForm
from employer.models import Jobs

from employer.forms import SignUpForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


class EmployerHomeView(TemplateView):
    template_name = "emp-home.html"


class AddJobView(CreateView):
    model = Jobs
    form_class = JobForm
    template_name = "emp-addjob.html"
    success_url = reverse_lazy("emp-alljobs")


class ListJobView(ListView):
    model = Jobs
    context_object_name = "jobs"
    template_name = "emp-listjob.html"



class JobDetailView(DetailView):
    model = Jobs
    context_object_name = "job"
    template_name = "emp-detailjob.html"
    pk_url_kwarg = "id"


class JobEditView(UpdateView):
    model = Jobs
    form_class = JobForm
    template_name = "emp-edit.html"
    success_url = reverse_lazy("emp-alljobs")
    pk_url_kwarg = "id"


# class JobDeleteView(View):
#     def get(self,request,id):
#         qs=Jobs.objects.get(id=id)
#         qs.delete()
#         return redirect("emp-alljobs")

class JobDeleteView(DeleteView):
    model = Jobs
    template_name = "jobconfirmdelete.html"
    success_url = reverse_lazy("emp-alljobs")
    pk_url_kwarg = "id"

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = "usersignup.html"
    success_url = reverse_lazy("emp-alljobs")

class SignInView(FormView):
    form_class = LoginForm
    template_name = "login.html"

    def post(self,request,*args,**kwargs):
         form=LoginForm(request.POST)
         if form.is_valid():
             uname=form.cleaned_data.get("username")
             pwd=form.cleaned_data.get("password")
             user=authenticate(request,username=uname,password=pwd)
             if user:
                 login(request,user)
                 return redirect("emp-alljobs")
             else:
                 return redirect(request,"login.html",{"form":form})

def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")

class ChangePasswordView(TemplateView):
    template_name = "changepassword.html"
    def post(self,request,*args,**kwargs):
        pwd=request.POST.get("pwd")
        uname=request.user
        user=authenticate(request,username=uname,password=pwd)
        if user:
            return redirect("password-reset")
        else:
            return render(request,self.template_name)

class PasswordResetView(TemplateView):
    template_name = "passwordreset.html"
    def post(self,request,*args,**kwargs):
        pwd1=request.POST.get("pwd1")
        pwd2=request.POST.get("pwd2")
        if pwd1!=pwd2:
            return render(request,self.template_name,{"msg":"incorrect password"})
        else:
            u=User.objects.get(username=request.user)
            u.set_password(pwd1)
            u.save()
            return redirect('signin')
