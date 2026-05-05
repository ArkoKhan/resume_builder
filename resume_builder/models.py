from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Resumes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s Resume - {self.title}"



class ResumeHeaders(models.Model):
    resume = models.OneToOneField(Resumes, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    resume_picture = models.ImageField(upload_to='resume_pictures/', blank=True, null=True)
    # resume_picture = CloudinaryField('image', folder='resume_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.resume.user.username}'s Resume Header - {self.full_name}"
    


class ResumeEducations(models.Model):
    resume = models.ForeignKey(Resumes, on_delete=models.CASCADE)
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=150)
    grade = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return f"{self.resume.user.username}'s {self.resume.title} Education"
    
    
    
class ResumeSkills(models.Model):
    SKILL_LEVEL_CHOICES = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Proficient', 'Proficient'),
        ('Highly Proficient', 'Highly Proficient'),
        ('Expert', 'Expert'),
    )
    
    resume = models.ForeignKey(Resumes, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    skill_level = models.CharField(max_length=30, choices=SKILL_LEVEL_CHOICES, default='Beginner')
    
    def __str__(self):
        return f"{self.resume.user.username}'s {self.resume.title} Skill - {self.skill_name}"
    
    
    
class ResumeExperiences(models.Model):
    resume = models.ForeignKey(Resumes, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150)
    job_title = models.CharField(max_length=150)
    starting_year = models.CharField(max_length=20)
    ending_year = models.CharField(max_length=20)
    job_description = models.TextField()
    
    def __str__(self):
        return f"{self.resume.user.username}'s {self.resume.title} Experience - {self.job_title} at {self.company_name}"
    
    
    
class ResumeLanguages(models.Model):
    
    LANG_LEVEL_CHOICES = (
        ('Conversational', 'Conversational'),
        ('Fluent', 'Fluent'),
        ('Native', 'Native'),
    )
    
    
    resume = models.ForeignKey(Resumes, on_delete=models.CASCADE)
    language_name = models.CharField(max_length=100)
    language_level = models.CharField(max_length=30, choices=LANG_LEVEL_CHOICES, default='Conversational')
    
    def __str__(self):
        return f"{self.resume.user.username}'s {self.resume.title} Language - {self.language_name}"
    
    
    
    
class ResumeSummaries(models.Model):
    resume = models.OneToOneField(Resumes, on_delete=models.CASCADE)
    summary_text  = models.TextField()
    
    def __str__(self):
        return f"{self.resume.user.username}'s {self.resume.title} Summary" 
    
    
    
    
    
    

class ResumeOtherSections(models.Model):
    resume = models.ForeignKey(Resumes, on_delete=models.CASCADE)
    header = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.resume.user.username}'s {self.resume.title} Other Section - {self.header}"
    
    
class ResumeOtherSectionItems(models.Model):
    other_section = models.ForeignKey(ResumeOtherSections, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.other_section.resume.user.username}'s {self.other_section.resume.title} Other Section Item - {self.title}"
    
    
class ResumeOtherSecShorts(models.Model):
    resume = models.ForeignKey(Resumes, on_delete=models.CASCADE)
    header = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.resume.user.username}'s {self.resume.title} Other Section Short - {self.header}"
    
    
class ResumeOtherSecShortItems(models.Model):
    other_sec_short = models.ForeignKey(ResumeOtherSecShorts, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    
    def __str__(self):
        return f"{self.other_sec_short.resume.user.username}'s {self.other_sec_short.resume.title} Other Section Short Item - {self.title}"
    
    
    
    

