from django.db import models
from employer.models import User
class CandidateProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="candidate")
    profile_pic=models.ImageField(upload_to="candprofiles")
    resume=models.FileField(upload_to="cvs",null=True)
    Qualification=models.CharField(max_length=120)
    skills=models.CharField(max_length=120)
    experience=models.PositiveIntegerField(default=0)
