from django.db import models

class Jobs(models.Model):
    job_title=models.CharField(max_length=150)
    company_name=models.CharField(max_length=150)
    location=models.CharField(max_length=120)
    salary=models.PositiveIntegerField(null=True)
    experience=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.job_title

