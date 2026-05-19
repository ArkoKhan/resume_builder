from django import forms
from .models import *



class ResumeForm(forms.ModelForm):
    class Meta:
        model= Resumes
        fields= ['title']
        labels = {
            'title': 'Resume Title',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Web Developer Resume',
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-800'
            }),
        }
        
        
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.widget.attrs['class'] = 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-800'
            field.widget.attrs['style'] = 'color: #1f2937;'
        
    

class ResumeHeaderForm(forms.ModelForm):
    class Meta:
        model = ResumeHeaders
        fields = ['full_name', 'email', 'phone_number', 'address', 'resume_picture']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'Enter Full Name',
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-800'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'example@email.com',
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-800'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': '+8801717123456',
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-800'
            }),
            'address': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Apartment, Street, City, State, Zip Code',
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-800'
            }),
            'resume_picture': forms.ClearableFileInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-800'
            }),
        }
        
    
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        
        self.fields['full_name'].label = 'Full Name'
        self.fields['email'].label = 'Email'
        self.fields['phone_number'].label = 'Phone Number'
        self.fields['address'].label = 'Address'
        
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-800'
            field.widget.attrs['style'] = 'color: #1f2937;'
            

class ResumeEducationForm(forms.ModelForm):
    class Meta:
        model = ResumeEducations
        fields = ['institution', 'degree', 'grade', 'passing_year']
        labels = {
            'institution': 'Institution Name',
            'degree': 'Degree',
            'grade': 'Grade/Score',
            'passing_year':'Passing Year'
        }
        
        widgets = {
            'institution': forms.TextInput(attrs={
                'placeholder': 'University or College Name',
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-800'
            }),
            'degree': forms.TextInput(attrs={
                'placeholder': 'Bachelor of Science in Computer Science',
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-800'
            }),
            'grade': forms.TextInput(attrs={
                'placeholder': 'CGPA(out of 4.0)/GPA(out of 5.0)',
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-800'
            }),
        }
                

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['style'] = 'color: #1f2937;'
                

class ResumeSkillForm(forms.ModelForm):
    class Meta:
        model = ResumeSkills
        fields = ['skill_name', 'skill_level']
        labels = {
            'skill_name': 'Skill Name',
            'skill_level': 'Skill Level',
        }
        
        widgets = {
            'skill_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-800',
                'placeholder': 'e.g. Python, React'
            }),
            'skill_level': forms.Select(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-800'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['style'] = 'color: #1f2937;'
        
        
        
class ResumeExperienceForm(forms.ModelForm):
    class Meta:
        model = ResumeExperiences
        fields = ['company_name', 'job_title', 'starting_year', 'ending_year', 'job_description']
        labels = {
            'company_name': 'Company Name',
            'job_title': 'Job Title',
            'starting_year': 'Starting Year',
            'ending_year': 'Ending Year',
            'job_description': 'Job Description',
        }
        
        widgets = {
            'company_name': forms.TextInput(attrs={
                'placeholder': 'Company Name',
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-800'
            }),
            'job_title': forms.TextInput(attrs={
                'placeholder': 'Job Title',
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-800'
            }),
            'starting_year': forms.TextInput(attrs={
                'placeholder': 'YYYY',
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-800'
            }),
            'ending_year': forms.TextInput(attrs={
                'placeholder': 'YYYY or Present',
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-800'
            }),
            'job_description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Describe your responsibilities, achievements...',
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-800'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['style'] = 'color: #1f2937;'
                
                
                
class ResumeLanguageForm(forms.ModelForm):
    class Meta:
        model = ResumeLanguages
        fields = ['language_name', 'language_level']
        labels = {
            'language_name': 'Language Name',
            'language_level': 'Language Level',
        }
        
        widgets = {
            'language_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-800',
                'placeholder': 'e.g. English, Spanish'
            }),
            'language_level': forms.Select(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-800'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['style'] = 'color: #1f2937;'


class ResumeSummaryForm(forms.ModelForm):
    class Meta:
        model = ResumeSummaries
        fields = ['summary_text']
        labels = {
            'summary_text': 'Professional Summary',
        }
        widgets = {
            'summary_text': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-800',
                'rows': 5,
                'placeholder': 'Write a brief summary about your professional background, skills, and career goals.'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['style'] = 'color: #1f2937;'
            
            
            
class ResumeOtherSectionsForm(forms.ModelForm):
    class Meta:
        model = ResumeOtherSections
        fields = ['header']
        labels = {
            'header': 'Section Header',
        }
        widgets = {
            'header': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-800'
            })
        }
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['style'] = 'color: #1f2937;'
            
            
class ResumeOtherSectionItemsForm(forms.ModelForm):
    class Meta:
        model = ResumeOtherSectionItems
        fields = ['title', 'description']
        labels = {
            'title': 'Item Title',
            'description': 'Item Description',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-800'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-800',
                'rows': 4,
            })
        }
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['style'] = 'color: #1f2937;'
            
            
            
class ResumeOtherSecShortsForm(forms.ModelForm):
    class Meta:
        model = ResumeOtherSecShorts
        fields = ['header']
        labels = {
            'header': 'Section Header',
        }
        widgets = {
            'header': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-800'
            })
        }
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['style'] = 'color: #1f2937;'
            
            
class ResumeOtherSecShortItemsForm(forms.ModelForm):
    class Meta:
        model = ResumeOtherSecShortItems
        fields = ['title']
        labels = {
            'title': 'Item Title',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-800'
            }),
        }
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['style'] = 'color: #1f2937;'