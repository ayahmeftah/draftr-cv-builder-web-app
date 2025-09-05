from django.urls import path
from . import views


urlpatterns = [
    path("",views.HomePageView.as_view(),name="homepage"),
    path("auth/signup/", views.SignUpView.as_view(), name="signup"),
    
    path("resumes/", views.TemplateListView.as_view(), name="template_list"),
    path("resumes/select/<int:template_id>/", views.select_template, name="select_template"),
    path("resumes/<int:resume_id>/personal/", views.PersonalInfoView.as_view(), name="resume_personal_info"),
    path("resumes/<int:resume_id>/preview/", views.ResumePreviewView.as_view(), name="resume_preview"),
    
    # Education
    path("resume/<int:resume_id>/education/", views.EducationListView.as_view(), name="education_list"),
    path("resume/<int:resume_id>/education/add/", views.EducationCreateView.as_view(), name="education_add"),
    path("resume/<int:resume_id>/education/<int:education_id>/delete/", views.EducationDeleteView.as_view(), name="education_delete"),
    path("resume/<int:resume_id>/education/<int:education_id>/edit/", views.EducationUpdateView.as_view(), name="education_edit"),
]
