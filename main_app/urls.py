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
    path("resumes/<int:resume_id>/educations/", views.EducationListView.as_view(), name="education_list"),
    path("resumes/<int:resume_id>/educations/add/", views.EducationCreateView.as_view(), name="education_add"),
    path("resumes/<int:resume_id>/educations/<int:education_id>/delete/", views.EducationDeleteView.as_view(), name="education_delete"),
    path("resumes/<int:resume_id>/educations/<int:education_id>/edit/", views.EducationUpdateView.as_view(), name="education_edit"),

    # Experience
    path("resumes/<int:resume_id>/experiences/", views.ExperienceListView.as_view(), name="experience_list"),
    path("resumes/<int:resume_id>/experiences/add/", views.ExperienceCreateView.as_view(), name="experience_add"),
    path("resumes/<int:resume_id>/experiences/<int:experience_id>/delete/", views.ExperienceDeleteView.as_view(), name="experience_delete"),
    path("resumes/<int:resume_id>/experiences/<int:experience_id>/edit/", views.ExperienceUpdateView.as_view(), name="experience_edit"),

    # Skill Category
    path("resumes/<int:resume_id>/skills/add-category/", views.SkillCategoryCreateView.as_view(), name="skill_category_add"),
]
