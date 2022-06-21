from django.urls import path
from candidate import views

urlpatterns=[
    path("home",views.CandidateHomeView.as_view(),name="cand-home"),
    path("profile/add",views.CandidateProfileView.as_view(),name="cand-addprofile"),
    path("profile/detail",views.CandidateProfileDetailView.as_view(),name="cand-profiledetail"),
    path("profile/change",views.CandidateProfileEditView.as_view(),name="cand-profedit"),
    path("jobs/all",views.CandidateJobListView.as_view(),name="cand-joblist"),
    path("jobs/detail/<int:id>",views.CandidateJobDetailViews.as_view(),name="cand-detailjob"),
    path("jobs/apply-now/<int:id>",views.apply_now,name="applynow")
]