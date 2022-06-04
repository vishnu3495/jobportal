from django import forms
from employer.models import Jobs
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class JobForm(forms.ModelForm):
    class Meta:
        model=Jobs
        fields="__all__"


class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())

class PasswordResetForm(forms.Form):
    password1=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField()

    def clean(self):
        cleaned_data=super().clean()
        pwd1=cleaned_data.get("password1")
        pwd2=cleaned_data.get("confirm_password")
        if pwd1!=pwd2:
            msg="password  miss match"
            self.add_error("password1",msg)
