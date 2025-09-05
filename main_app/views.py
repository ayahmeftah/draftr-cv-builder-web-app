from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView, DeleteView
from django.contrib.auth import login
from django.urls import reverse_lazy, reverse
from . import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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


class TemplateListView(LoginRequiredMixin, ListView):
    model = models.Template
    template_name = "resumes/template_list.html"
    context_object_name = "templates"


def select_template(request, template_id):
    template = get_object_or_404(models.Template, pk=template_id)
    resume = models.Resume.objects.create(
        user=request.user,
        template=template,
        resume_name="",
        candidate_name="",
        email=request.user.email,
        mobile="")

    return redirect('resume_personal_info', resume_id=resume.id)


class PersonalInfoView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Resume
    form_class = forms.ResumePersonalForm
    template_name = "resumes/personal_info_form.html"
    pk_url_kwarg = "resume_id"

    def get_success_url(self):
        return reverse_lazy('education_list', kwargs={'resume_id': self.object.id})

    def test_func(self):
        resume = self.get_object()
        return resume.user == self.request.user

class ResumePreviewView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = models.Resume
    template_name = "cv_templates/template1.html"
    pk_url_kwarg = "resume_id"
    context_object_name = "resume"

    def test_func(self):
        resume = self.get_object()
        return resume.user == self.request.user

# Education Views

class EducationCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.Education
    form_class = forms.EducationForm
    template_name = "educations/education_form.html"

    def form_valid(self, form):
        resume = get_object_or_404(models.Resume, id=self.kwargs['resume_id'], user=self.request.user)
        form.instance.resume = resume
        form.save()
        return redirect("education_list", resume_id=resume.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resume"] = get_object_or_404(models.Resume, id=self.kwargs['resume_id'], user=self.request.user)
        return context

    def test_func(self):
        resume = get_object_or_404(models.Resume, id=self.kwargs['resume_id'])
        return resume.user == self.request.user

class EducationListView(LoginRequiredMixin, ListView):
    model = models.Education
    template_name = "educations/education_list.html"
    context_object_name = "educations"

    def get_queryset(self):
        resume = get_object_or_404(models.Resume, id=self.kwargs['resume_id'], user=self.request.user)
        return models.Education.objects.filter(resume=resume)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resume"] = get_object_or_404(models.Resume, id=self.kwargs['resume_id'], user=self.request.user)
        return context

class EducationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Education
    pk_url_kwarg = "education_id"

    def get_success_url(self):
        return redirect("education_list", resume_id=self.object.resume.id).url

    def test_func(self):
        education = self.get_object()
        return education.resume.user == self.request.user
    

class EducationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Education
    form_class = forms.EducationForm
    template_name = "educations/education_form.html"
    pk_url_kwarg = "education_id"

    def get_success_url(self):
        return redirect("education_list", resume_id=self.object.resume.id).url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resume"] = self.object.resume
        return context

    def test_func(self):
        education = self.get_object()
        return education.resume.user == self.request.user
    

# Experience Views

class ExperienceCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.Experience
    form_class = forms.ExperienceForm
    template_name = "experiences/experience_form.html"

    def form_valid(self, form):
        resume = get_object_or_404(models.Resume, id=self.kwargs['resume_id'], user=self.request.user)
        form.instance.resume = resume
        form.save()
        return redirect("experience_list", resume_id=resume.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resume"] = get_object_or_404(models.Resume, id=self.kwargs['resume_id'], user=self.request.user)
        return context

    def test_func(self):
        resume = get_object_or_404(models.Resume, id=self.kwargs['resume_id'])
        return resume.user == self.request.user
    
class ExperienceListView(LoginRequiredMixin, ListView):
    model = models.Experience
    template_name = "experiences/experience_list.html"
    context_object_name = "experiences"

    def get_queryset(self):
        resume = get_object_or_404(models.Resume, id=self.kwargs['resume_id'], user=self.request.user)
        return models.Experience.objects.filter(resume=resume)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resume"] = get_object_or_404(models.Resume, id=self.kwargs['resume_id'], user=self.request.user)
        return context
    
class ExperienceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Experience
    pk_url_kwarg = "experience_id"

    def get_success_url(self):
        return redirect("experience_list", resume_id=self.object.resume.id).url

    def test_func(self):
        experience = self.get_object()
        return experience.resume.user == self.request.user
    

class ExperienceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Experience
    form_class = forms.ExperienceForm
    template_name = "experiences/experience_form.html"
    pk_url_kwarg = "experience_id"

    def get_success_url(self):
        return redirect("experience_list", resume_id=self.object.resume.id).url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resume"] = self.object.resume
        return context

    def test_func(self):
        experience = self.get_object()
        return experience.resume.user == self.request.user
    

# Skill Category Views

class SkillCategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.SkillCategory
    form_class = forms.SkillCategoryForm
    template_name = "skills/skill_category_form.html"

    def form_valid(self, form):
        resume = get_object_or_404(models.Resume, id=self.kwargs['resume_id'], user=self.request.user)
        form.instance.resume = resume
        form.save()
        return redirect("skill_list", resume_id=resume.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resume"] = get_object_or_404(models.Resume, id=self.kwargs['resume_id'], user=self.request.user)
        return context

    def test_func(self):
        resume = get_object_or_404(models.Resume, id=self.kwargs['resume_id'])
        return resume.user == self.request.user


class SkillCategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.SkillCategory
    pk_url_kwarg = "category_id"

    def get_success_url(self):
        return redirect("skill_list", resume_id=self.object.resume.id).url

    def test_func(self):
        category = self.get_object()
        return category.resume.user == self.request.user


# Skill Views

def skill_list(request, resume_id):
    resume = get_object_or_404(models.Resume, id=resume_id, user=request.user)
    categories = resume.skill_categories.prefetch_related('skills').all()
    return render(request, "skills/skill_list.html", {
        "resume": resume,
        "categories": categories
    })

class SkillCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.Skill
    form_class = forms.SkillForm
    template_name = "skills/skill_form.html"

    def form_valid(self, form):
        category = get_object_or_404(models.SkillCategory, id=self.kwargs['category_id'])
        form.instance.skill_category = category
        form.save()
        return redirect("skill_list", resume_id=category.resume.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = get_object_or_404(models.SkillCategory, id=self.kwargs['category_id'])
        return context

    def test_func(self):
        category = get_object_or_404(models.SkillCategory, id=self.kwargs['category_id'])
        return category.resume.user == self.request.user
    
class SkillDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Skill
    pk_url_kwarg = "skill_id"

    def get_success_url(self):
        return redirect("skill_list", resume_id=self.object.skill_category.resume.id).url

    def test_func(self):
        skill = self.get_object()
        return skill.skill_category.resume.user == self.request.user
    
class SkillUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Skill
    form_class = forms.SkillForm
    template_name = "skills/skill_form.html"
    pk_url_kwarg = "skill_id"

    def get_success_url(self):
        return redirect("skill_list", resume_id=self.object.skill_category.resume.id).url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.object.skill_category
        return context

    def test_func(self):
        skill = self.get_object()
        return skill.skill_category.resume.user == self.request.user