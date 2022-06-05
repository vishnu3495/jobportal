from django.urls import path
from employer import views

urlpatterns = [
path("home",views.EmployerHomeView.as_view(),name="emp-home"),
path("jobs/add",views.AddJobView.as_view(),name="emp-addjob"),
path("jobs/all",views.ListJobView.as_view(),name="emp-alljobs"),
path("jobs/detail/<int:id>",views.JobDetailView.as_view(),name="emp-jobdetail"),
path("jobs/change/<int:id>",views.JobEditView.as_view(),name="emp-editjob"),
path("jobs/remove/<int:id>",views.JobDeleteView.as_view(),name="emp-deletejob"),
path("users/account/signup",views.SignUpView.as_view(),name="signup"),
path("users/account/signin",views.SignInView.as_view(),name="signin"),
path("users/accounts/signout",views.signout_view,name="signout"),
path("users/password/change",views.ChangePasswordView.as_view(),name="password-change"),
path("users/password/reset",views.PasswordResetView.as_view(),name="password-reset"),
path("profile/add",views.CompanyProfileView.as_view(),name="emp-addprofile"),
path("profile/detail",views.EmpViewProfileView.as_view(),name="emp-viewprofile"),
path("profile/edit/<int:id>",views.EmpProfileEditView.as_view(),name="emp-editprofile")


]