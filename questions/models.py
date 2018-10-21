from django.db import models
from datetime import datetime

# Create your models here.
class Question(models.Model):
    SUBJECT_OPTIONS = [('ISTQB','ISTQB'),('OOP','Object Orientated Programming'),('Personal','Personal question'),('CAN','CAN'),('Logic','Logical question')]
    LEVEL_OPTIONS = [('Junior','Low'),('Profesional','Medium'),('Senior','High'),('N/A','Not applicable')]

    question = models.CharField(max_length=200)
    answer = models.TextField(null=True)
    subject = models.CharField(choices=SUBJECT_OPTIONS, max_length=200)
    dificulty_level = models.CharField(default='N/A', choices=LEVEL_OPTIONS, max_length=200)
    added_by = models.CharField(max_length=200)
    # created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.question # this indicates the displayed value for each item under admin/questions ( text is a collumn of the table questions) 
    class Meta:
        verbose_name_plural = "Questions" # this changes the plural from admin page avooiding double 's'