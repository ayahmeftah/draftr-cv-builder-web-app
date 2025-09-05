from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView, DeleteView
from django.contrib.auth import login
from django.urls import reverse_lazy
from . import models, forms

# Create your views here.


class HomePageView(TemplateView):
    template_name = "homepage.html"


class SignUpView(CreateView):
    form_class = forms.CustomUserCreationForm
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
        resume_name="",
        candidate_name="",
        email=request.user.email,
        mobile="")

    return redirect('resume_personal_info', resume_id=resume.id)


class PersonalInfoView(UpdateView):
    model = models.Resume
    form_class = forms.ResumePersonalForm
    template_name = "resumes/personal_info_form.html"
    pk_url_kwarg = "resume_id"

    def get_success_url(self):
        return reverse_lazy('education_list', kwargs={'resume_id': self.object.id})


class ResumePreviewView(DetailView):
    model = models.Resume
    template_name = "cv_templates/template1.html"
    pk_url_kwarg = "resume_id"
    context_object_name = "resume"
    

# Education Views

class EducationCreateView(CreateView):
    model = models.Education
    form_class = forms.EducationForm
    template_name = "educations/education_form.html"

    def form_valid(self, form):
        resume = get_object_or_404(models.Resume, id=self.kwargs['resume_id'])
        form.instance.resume = resume
        form.save()
        return redirect("education_list", resume_id=resume.id)
    
class EducationListView(ListView):
    model = models.Education
    template_name = "educations/education_list.html"
    context_object_name = "educations"

    def get_queryset(self):
        resume = get_object_or_404(models.Resume, id=self.kwargs['resume_id'])
        return models.Education.objects.filter(resume=resume)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resume"] = get_object_or_404(models.Resume, id=self.kwargs['resume_id'])
        return context
    
class EducationDeleteView(DeleteView):
    model = models.Education
    pk_url_kwarg = "education_id"

    def get_success_url(self):
        return redirect("education_list", resume_id=self.object.resume.id).url
    
class EducationUpdateView(UpdateView):
    model = models.Education
    form_class = forms.EducationForm
    template_name = "education_form.html"
    pk_url_kwarg = "education_id"

    def get_success_url(self):
        return redirect("education_list", resume_id=self.object.resume.id).url