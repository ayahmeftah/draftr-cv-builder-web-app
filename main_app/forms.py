from django import forms
from . import models


class ResumePersonalForm(forms.ModelForm):

    class Meta:
        model = models.Resume
        fields = [
            'candidate_name', 'job_title', 'candidate_image', 'profile',
            'location', 'email', 'mobile', 'linkedin_link',
            'additional_link_name', 'additional_link'
        ]
