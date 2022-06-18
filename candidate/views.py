from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class CandidateHomeView(TemplateView):
    template_name = "can-home.html"