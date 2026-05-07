from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .summary_generator import SummaryGenerator
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import render_to_string
from weasyprint import HTML
from cloudinary_api import Image
import uuid
import os


# Create your views here.

image = Image()

def app_home(request):
    if request.user.is_authenticated:
        
    
        resumes = Resumes.objects.filter(user=request.user)
        
        context={
            'title': 'Resume Builder',
            'resumes': resumes,
        }
        
        return render(request, 'resume_builder/app_home.html', context)
    else:
        messages.info(request, 'Please login to access the resume builder.')
        return redirect('login')



@login_required
def show_resume(request, pk):
    resume = Resumes.objects.get(pk=pk)
    resume_header = ResumeHeaders.objects.get(resume=resume)
    resume_educations = ResumeEducations.objects.filter(resume=resume)
    resume_skills = ResumeSkills.objects.filter(resume=resume)
    resume_experiences = ResumeExperiences.objects.filter(resume=resume)
    resume_languages = ResumeLanguages.objects.filter(resume=resume)
    resume_summary = ResumeSummaries.objects.filter(resume=resume).first()
    others= ResumeOtherSections.objects.filter(resume=resume)
    other_items = ResumeOtherSectionItems.objects.all()
    other_shorts = ResumeOtherSecShorts.objects.filter(resume=resume)
    other_short_items = ResumeOtherSecShortItems.objects.all()
    
    context = {
        'resume': resume,
        'cv_head': resume_header,
        'edications': resume_educations,
        'skills': resume_skills,
        'experiences': resume_experiences,
        'languages': resume_languages,
        'summary': resume_summary,
        'others': others,
        'other_items': other_items,
        'other_shorts': other_shorts,
        'other_short_items': other_short_items,
    }
    
    return render(request, 'resume_builder/show_resume.html', context)


# Create Resume

@login_required
def create_resume(request):
    if request.method == 'POST':
        resume_form = ResumeForm(request.POST)
        resume_header_form = ResumeHeaderForm(request.POST, request.FILES)
        if resume_form.is_valid() and resume_header_form.is_valid():
            resume = resume_form.save(commit=False)
            resume.user = request.user
            resume.unique_name = f"{request.user.username}@{uuid.uuid4().hex[:8]}"
            resume.save()
            resume_header = resume_header_form.save(commit=False)
            resume_header.resume = resume
            resume_header.resume_picture_link = image.upload(resume_header.resume_picture.url, resume.unique_name)
            resume_header.save()
            return redirect('add_education', pk= resume.pk)
    else:
        resume_form = ResumeForm()
        resume_header_form = ResumeHeaderForm()
        
    context = {
        'resume_form': resume_form,
        'resume_header_form': resume_header_form,
        'title': 'Create Resume',
        'subtitle': 'Your personal information and what is the reason of creating this resume.',
    }
    
    return render(request, 'resume_builder/resume_form_media.html', context)



def add_education(request, pk):
    resume = Resumes.objects.get(pk=pk)
    data = ResumeEducations.objects.filter(resume=resume)
    if request.method == 'POST':
        form = ResumeEducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.resume = resume
            education.save()
            return redirect('add_education', pk=resume.pk)
    else:
        form = ResumeEducationForm()
        
    context = {
        'form': form,
        'data': data,
        'title': 'Add Education',
        'subtitle': 'Your educational background and qualifications.',
        'next_btn': 'add_experience',
        'resume': resume,
        
    }
    
    return render(request, 'resume_builder/resume_form_multi.html', context)

def add_experience(request, pk):
    resume = Resumes.objects.get(pk=pk)
    data = ResumeExperiences.objects.filter(resume=resume)
    if request.method == 'POST':
        form = ResumeExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.resume = resume
            experience.save()
            return redirect('add_experience', pk=resume.pk)
    else:
        form = ResumeExperienceForm()
        
    context = {
        'form': form,
        'data': data,
        'title': 'Add Experience',
        'subtitle': 'Your work experience and professional background.',
        'next_btn': 'add_skill',
        'resume': resume,
    }
    
    return render(request, 'resume_builder/resume_form_multi.html', context)



def add_skill(request, pk):
    resume =Resumes.objects.get(pk=pk)
    data = ResumeSkills.objects.filter(resume=resume)
    if request.method == 'POST':
        form = ResumeSkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.resume = resume
            skill.save()
            return redirect('add_skill', pk=resume.pk)
        
    else:
        form = ResumeSkillForm()
    
    context = {
        'form': form,
        'data': data,
        'title': 'Add Skill',
        'subtitle': 'Your skills and proficiencies.',
        'next_btn': 'add_language',
        'resume': resume,
    }
    
    return render(request, 'resume_builder/resume_form_multi.html', context)


def add_language(request, pk):
    resume = Resumes.objects.get(pk=pk)
    data = ResumeLanguages.objects.filter(resume=resume)
    if request.method == 'POST':
        form = ResumeLanguageForm(request.POST)
        if form.is_valid():
            language = form.save(commit=False)
            language.resume = resume
            language.save()
            return redirect('add_language', pk=resume.pk)
        
        
    else:
        form = ResumeLanguageForm()
    
    context = {
        'form': form,
        'data': data,
        'title': 'Add Language',
        'subtitle': 'Languages you are proficient in.',
        'next_btn': 'add_summary',
        'resume': resume,
    }
    
    return render(request, 'resume_builder/resume_form_multi.html', context)



def add_summary(request, pk):
    resume = Resumes.objects.get(pk=pk)
    if request.method == 'POST':
        form = ResumeSummaryForm(request.POST)
        
        if 'generate' in request.POST:
            skills = ResumeSkills.objects.filter(resume=resume)
            occupation = resume.title

            generator = SummaryGenerator()
            summary_txt = generator.generate_summary(occupation, skills)
            
            form = ResumeSummaryForm({
                **request.POST,
                'summary_text': summary_txt,
            })
        elif 'save' in request.POST:
            if form.is_valid():
                summary = form.save(commit=False)
                summary.resume = resume
                summary.save()
                return redirect('show_resume', pk=resume.pk)        
    else:
        form = ResumeSummaryForm()
        
    context = {
        'form': form,
        'title': 'Add Summary',
        'subtitle': 'A brief summary or objective statement for your resume.',
        'resume': resume,
    }
    
    return render(request, 'resume_builder/resume_form_single.html', context)


# Update views goes here

def update_info(request, pk):
    resume_header = ResumeHeaders.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = ResumeHeaderForm(request.POST, request.FILES, instance=resume_header)
        if form.is_valid():
            # if 'resume_picture' in request.FILES:
            #     # Delete old file if it exists
            #     if resume_header.resume_picture:
            #         resume_header.resume_picture.delete(save=False)
            resume_header.resume_picture_link = image.upload(resume_header.resume_picture.url, resume_header.resume.unique_name)
            form.save()
            return redirect('show_resume', resume_header.resume.pk)
    else:
        form = ResumeHeaderForm(instance=resume_header)
        
    context = {
        'form': form,
        'title': 'Update Personal Info',
        
    }
    
    return render(request, 'resume_builder/info_update.html', context)


def update_education(request, pk):
    resume = Resumes.objects.get(pk=pk)
    data = ResumeEducations.objects.filter(resume=resume)
    if request.method == 'POST':
        form = ResumeEducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.resume = resume
            education.save()
            return redirect('update_education', pk=resume.pk)
    else:
        form = ResumeEducationForm()
        
    context = {
        'form': form,
        'data': data,
        'title': 'Add Education',
        'subtitle': 'Your educational background and qualifications.',
        'resume': resume,
        
    }
    
    return render(request, 'resume_builder/resume_update_multi.html', context)

def update_experience(request, pk):
    resume = Resumes.objects.get(pk=pk)
    data = ResumeExperiences.objects.filter(resume=resume)
    if request.method == 'POST':
        form = ResumeExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.resume = resume
            experience.save()
            return redirect('update_experience', pk=resume.pk)
    else:
        form = ResumeExperienceForm()
        
    context = {
        'form': form,
        'data': data,
        'title': 'Add Experience',
        'subtitle': 'Your work experience and professional background.',
        'resume': resume,
    }
    
    return render(request, 'resume_builder/resume_update_multi.html', context)



def update_skill(request, pk):
    resume =Resumes.objects.get(pk=pk)
    data = ResumeSkills.objects.filter(resume=resume)
    if request.method == 'POST':
        form = ResumeSkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.resume = resume
            skill.save()
            return redirect('update_skill', pk=resume.pk)
        
    else:
        form = ResumeSkillForm()
    
    context = {
        'form': form,
        'data': data,
        'title': 'Add Skill',
        'subtitle': 'Your skills and proficiencies.',
        'resume': resume,
    }
    
    return render(request, 'resume_builder/resume_update_multi.html', context)


def update_language(request, pk):
    resume = Resumes.objects.get(pk=pk)
    data = ResumeLanguages.objects.filter(resume=resume)
    if request.method == 'POST':
        form = ResumeLanguageForm(request.POST)
        if form.is_valid():
            language = form.save(commit=False)
            language.resume = resume
            language.save()
            return redirect('update_language', pk=resume.pk)
        
        
    else:
        form = ResumeLanguageForm()
    
    context = {
        'form': form,
        'data': data,
        'title': 'Add Language',
        'subtitle': 'Languages you are proficient in.',
        'resume': resume,
    }
    
    return render(request, 'resume_builder/resume_update_multi.html', context)

def update_summary(request, pk):
    summary = ResumeSummaries.objects.get(pk=pk)
    resume = summary.resume
    if request.method == 'POST':
        form = ResumeSummaryForm(request.POST, instance=summary)
        
        if 'generate' in request.POST:
            skills = ResumeSkills.objects.filter(resume=resume)
            occupation = resume.title

            
            generator = SummaryGenerator()
            summary_txt = generator.generate_summary(occupation, skills)
            
            form = ResumeSummaryForm(
                {**request.POST, 'summary_text': summary_txt,},
                instance=summary
                )
        elif 'save' in request.POST:
            if form.is_valid():
                form.save()
                return redirect('show_resume', pk=resume.pk)        
    else:
        form = ResumeSummaryForm(instance=summary)
        
    context = {
        'form': form,
        'title': 'Add Summary',
        'subtitle': 'A brief summary or objective statement for your resume.',
        'resume': resume,
    }
    
    return render(request, 'resume_builder/resume_form_single.html', context)






# download template view

def download_template(request, pk):
    resume = Resumes.objects.get(pk=pk)
    resume_header = ResumeHeaders.objects.get(resume=resume)
    resume_educations = ResumeEducations.objects.filter(resume=resume)
    resume_skills = ResumeSkills.objects.filter(resume=resume)
    resume_experiences = ResumeExperiences.objects.filter(resume=resume)
    resume_languages = ResumeLanguages.objects.filter(resume=resume)
    resume_summary = ResumeSummaries.objects.filter(resume=resume).first()
    
    image_url = None
    if resume_header.resume_picture:
        image_url = resume_header.resume_picture.url
    
    context = {
        'resume': resume,
        'cv_head': resume_header,
        'edications': resume_educations,
        'skills': resume_skills,
        'experiences': resume_experiences,
        'languages': resume_languages,
        'summary': resume_summary,
        'resume_image_url': image_url,
    }
    
    return render(request, 'resume_builder/download_resume.html', context)


class ResumePDFView(View):
    def get(self, request, pk):
            resume = Resumes.objects.get(pk=pk)
            resume_header = ResumeHeaders.objects.get(resume=resume)
            resume_educations = ResumeEducations.objects.filter(resume=resume)
            resume_skills = ResumeSkills.objects.filter(resume=resume)
            resume_experiences = ResumeExperiences.objects.filter(resume=resume)
            resume_languages = ResumeLanguages.objects.filter(resume=resume)
            resume_summary = ResumeSummaries.objects.filter(resume=resume).first()
            others= ResumeOtherSections.objects.filter(resume=resume)
            other_items = ResumeOtherSectionItems.objects.all()
            other_shorts = ResumeOtherSecShorts.objects.filter(resume=resume)
            other_short_items = ResumeOtherSecShortItems.objects.all()
    
            image_url = None
            if resume_header.resume_picture:
                image_url = resume_header.resume_picture.url
            
            context = {
                'resume': resume,
                'cv_head': resume_header,
                'edications': resume_educations,
                'skills': resume_skills,
                'experiences': resume_experiences,
                'languages': resume_languages,
                'summary': resume_summary,
                'others': others,
                'other_items': other_items,
                'other_shorts': other_shorts,
                'other_short_items': other_short_items,
                'resume_image_url': image_url,
            }
            
            html_string = render_to_string('resume_builder/download_resume.html', context)
            
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="resume of {resume_header.full_name} for {resume.title}.pdf"'
            
            HTML(
                string=html_string,
                base_url=request.build_absolute_uri()
                ).write_pdf(response)
            
            return response



# All delete views goes here

def delete_skill(request, pk):
    obj = ResumeSkills.objects.get(pk=pk)
    reusme_pk = obj.resume.pk
    obj.delete()
    return redirect('show_resume', pk=reusme_pk)

def delete_language(request, pk):
    obj = ResumeLanguages.objects.get(pk=pk)
    reusme_pk = obj.resume.pk
    obj.delete()
    return redirect('show_resume', pk=reusme_pk)

def delete_experience(request, pk):
    obj = ResumeExperiences.objects.get(pk=pk)
    reusme_pk = obj.resume.pk
    obj.delete()
    return redirect('show_resume', pk=reusme_pk)

def delete_education(request, pk):
    obj = ResumeEducations.objects.get(pk=pk)
    reusme_pk = obj.resume.pk
    obj.delete()
    return redirect('show_resume', pk=reusme_pk)


# Resume Delete View

def delete_resume(request, pk):
    resume = Resumes.objects.get(pk=pk)
    try:
        resume_head = ResumeHeaders.objects.get(resume=resume)
        
        if resume_head.resume_picture:
            resume_head.resume_picture.delete(save=False)
        
    except ResumeHeaders.DoesNotExist:
        pass
    
    resume.delete()
    return redirect('app_home')






# Other Sections

def add_other_sec(request, pk):
    resume = Resumes.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = ResumeOtherSectionsForm(request.POST)
        if form.is_valid():
            section = form.save(commit=False)
            section.resume = resume
            section.save()
            return redirect('show_resume', resume.pk)
    else:
        form = ResumeOtherSectionsForm()
    
    context = {
        'form': form,
        'resume': resume,
        'title': 'Add New Section'
    }
    
    return render(request, 'resume_builder/other_sec.html', context)

def delete_sec(request, pk):
    obj = ResumeOtherSections.objects.get(pk=pk)
    resume_pk = obj.resume.pk
    obj.delete()
    return redirect('show_resume', resume_pk)


def add_other_sec_item(request, pk):
    section = ResumeOtherSections.objects.get(pk=pk)
    resume = Resumes.objects.get(pk=section.resume.pk)
    data = ResumeOtherSectionItems.objects.filter(other_section=section)
    
    
    if request.method == 'POST':
        form = ResumeOtherSectionItemsForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.other_section = section
            item.save()
            return redirect('add_other_sec_item', section.pk)
    else:
        form = ResumeOtherSectionItemsForm()
    
    context = {
        'form': form,
        'section': section,
        'resume': resume,
        'data': data,
        'title': section.header,
    }
    
    return render(request, 'resume_builder/other_sec_item.html', context)


def delete_item(request, pk):
    obj = ResumeOtherSectionItems.objects.get(pk=pk)
    resume_pk = obj.other_section.resume.pk
    obj.delete()
    return redirect('show_resume', resume_pk)



def add_other_short(request, pk):
    resume = Resumes.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = ResumeOtherSecShortsForm(request.POST)
        if form.is_valid():
            section = form.save(commit=False)
            section.resume = resume
            section.save()
            return redirect('show_resume', resume.pk)
    else:
        form = ResumeOtherSecShortsForm()
    
    context = {
        'form': form,
        'resume': resume,
    }
    
    return render(request, 'resume_builder/other_sec.html', context)


def delete_short_sec(request, pk):
    obj = ResumeOtherSecShorts.objects.get(pk=pk)
    resume_pk = obj.resume.pk
    obj.delete()
    return redirect('show_resume', resume_pk)

def add_other_short_item(request, pk):
    section = ResumeOtherSecShorts.objects.get(pk=pk)
    resume = Resumes.objects.get(pk=section.resume.pk)
    data = ResumeOtherSecShortItems.objects.filter(other_sec_short=section)
    
    
    if request.method == 'POST':
        form = ResumeOtherSecShortItemsForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.other_sec_short = section
            item.save()
            return redirect('add_other_short_item', section.pk)
    else:
        form = ResumeOtherSecShortItemsForm()
    
    context = {
        'form': form,
        'section': section,
        'resume': resume,
        'data': data,
        'title': section.header,
    }
    
    return render(request, 'resume_builder/other_sec_item_short.html', context)


def delete_item_short(request, pk):
    obj = ResumeOtherSecShortItems.objects.get(pk=pk)
    resume_pk = obj.other_sec_short.resume.pk
    obj.delete()
    return redirect('show_resume', resume_pk)