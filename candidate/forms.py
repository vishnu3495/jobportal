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