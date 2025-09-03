from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Template(models.Model):
    template_name = models.CharField(max_length=100)
    preview_image = models.ImageField(upload_to="cv-templates-images/")
    template_path = models.CharField(max_length=200)
    candidate_img_available = models.BooleanField(default=False)

    class Meta:
        db_table = "cv_templates"
    
    def __str__(self):
        return f"cv template name: {self.template_name} in {self.template_path}"

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="resumes")
    template = models.ForeignKey(Template, on_delete=models.CASCADE, related_name="resumes")

    resume_name = models.CharField(max_length=255)
    candidate_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=150)
    candidate_image = models.ImageField(upload_to="candidates/", null=True, blank=True)
    profile = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=255)
    mobile = models.CharField(max_length=20)
    linkedin_link = models.URLField(null=True, blank=True)
    additional_link_name = models.CharField(max_length=100, null=True, blank=True)
    additional_link = models.URLField(null=True, blank=True)

    class Meta:
        db_table = "resumes"

    def __str__(self):
        return f"Resume: {self.resume_name} ({self.candidate_name})"
    

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="educations")
    
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "educations"

    def __str__(self):
        return f"{self.degree} at {self.school}"
    

class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="experiences")

    company = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "experiences"

    def __str__(self):
        return f"{self.role} at {self.company}"
    

class SkillCategory(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="skill_categories")

    skill_category_title = models.CharField(max_length=150)

    class Meta:
        db_table = 'skill_categories'

    def __str__(self):
        return f"Skill Category: {self.skill_category_title}"


class Skill(models.Model):
    skill_category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name="skills")

    skill_name = models.CharField(max_length=150)
    level = models.CharField(max_length=100)

    class Meta:
        db_table = 'skills'

    def __str__(self):
        return f"{self.skill_name} ({self.level})"
    
class Certification(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="certifications")

    certification_name = models.CharField(max_length=255)
    issued_by = models.CharField(max_length=255)
    credential_url = models.URLField(null=True, blank=True)

    class Meta:
        db_table = "certifications"

    def __str__(self):
        return f"Certification: {self.certification_name} from {self.issued_by}"


class Project(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="projects")

    project_title = models.CharField(max_length=255)
    project_description = models.TextField(null=True, blank=True)
    project_link = models.URLField(null=True, blank=True)

    class Meta:
        db_table = "projects"

    def __str__(self):
        return f"Project: {self.project_title}"