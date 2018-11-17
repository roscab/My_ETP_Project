from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Candidate

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question','subject','added_by']

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name']
