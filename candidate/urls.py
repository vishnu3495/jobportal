from django.urls import path
from candidate import views

urlpatterns=[
    path("home",views.CandidateHomeView.as_view(),name="cand-home"),
    path("profile/add",views.CandidateProfileView.as_view(),name="cand-addprofile")
]