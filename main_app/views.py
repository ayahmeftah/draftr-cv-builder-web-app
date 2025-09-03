from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from . import models, forms

# Create your views here.

class HomePageView(TemplateView):
    template_name = "homepage.html"


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)


class TemplateListView(ListView):
    model = models.Template
    template_name = "resumes/template_list.html"
    context_object_name = "templates"


def select_template(request, template_id):
    template = models.Template.objects.get(pk=template_id)
    resume = models.Resume.objects.create(
        user=request.user,
        template=template,
        resume_name= "",
        candidate_name=request.user.get_full_name() or request.user.username,
        email=request.user.email,
        mobile=""
        )
    
    return redirect('resume_personal_info', resume_id=resume.id)
