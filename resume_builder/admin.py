from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Resumes)
admin.site.register(ResumeHeaders)
admin.site.register(ResumeEducations)
admin.site.register(ResumeSkills)
admin.site.register(ResumeExperiences)
admin.site.register(ResumeLanguages)
admin.site.register(ResumeSummaries)
admin.site.register(ResumeOtherSections)
admin.site.register(ResumeOtherSectionItems)
admin.site.register(ResumeOtherSecShorts)
admin.site.register(ResumeOtherSecShortItems)
