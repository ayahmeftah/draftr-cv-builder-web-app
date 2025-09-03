from django.urls import path
from . import views


urlpatterns = [
    path("",views.HomePageView.as_view(),name="homepage"),
    path("auth/signup/", views.SignUpView.as_view(), name="signup"),
    path("resumes/", views.TemplateListView.as_view(), name="template_list"),
    path("resumes/select/<int:template_id>/", views.select_template, name="select_template"),
    path("resumes/<int:resume_id>/personal/", views.PersonalInfoView.as_view(), name="resume_personal_info"),
]
