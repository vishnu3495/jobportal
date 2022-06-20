from django import forms
from candidate.models import CandidateProfile


class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model=CandidateProfile
        exclude=("user",)
        widgets={
            "profile_pic":forms.FileInput(attrs={"class":"form-select"}),
            "Qualification":forms.TextInput(attrs={"class":"form-control rounded-pill"}),
            "skills":forms.TextInput(attrs={"class":"form-control rounded-pill"}),
            "experience":forms.NumberInput(attrs={"class":"form-control rounded-pill"})

        }

class CandidateProfileUpdateForm(forms.ModelForm):

    first_name=forms.CharField(max_length=150)
    last_name=forms.CharField(max_length=100)
    phone=forms.CharField(max_length=150)
    email=forms.EmailField()

    class Meta:
        model=CandidateProfile
        fields=['first_name',
                'last_name',
                'phone',
                'email',
                'profile_pic',
                "resume",
                "Qualification",
                "skills",
                "experience"


                ]

