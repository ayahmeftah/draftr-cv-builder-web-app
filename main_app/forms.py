from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class ResumePersonalForm(forms.ModelForm):

    class Meta:
        model = models.Resume
        fields = [
            'candidate_name', 'resume_name','job_title', 'candidate_image', 'profile',
            'location', 'email', 'mobile', 'linkedin_link',
            'additional_link_name', 'additional_link'
        ]

class EducationForm(forms.ModelForm):
    class Meta:
        model = models.Education
        fields = ["school", "degree", "start_date", "end_date", "is_current", "description"]

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = models.Experience
        fields = ["company", "role", "start_date", "end_date", "is_current", "description"]