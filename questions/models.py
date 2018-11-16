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

class Candidate(models.Model):
    RECRUITER_OPTIONS = [('Guillermo Lopez','Guillermo Lopez'),('Vernonica Mendes','Verónica Mendes'),('Alberto Arjona','Alberto Arjona'),('Luisa Cabrera','Luisa Cabrera'),('Oscar Penon','Oscar Penon'),('Monika Szymanska','Monika Szymanska')]
    LEVEL_OPTIONS = [('Junior','Junior'),('Junior-Low','Junior-Low'),('Junior-High','Junior-High'),('Profesional','Profesional'),('Profesional-Low','Profesional-Low'),('Profesional-High','Profesional-High'),('Senior','Senior'),('Senior-Low','Senior-Low'),('Senior-High','Senior-High')]
    STATUS_OPTIONS = [('Pass recruiter interview','Pass recruiter interview'),('Rejected by recruiter','Rejected by recruiter'),('Pass technical interview','Pass technical interview'),('Rejected by technical interviewer','Rejected by technical interviewer'),('Pass BUL intreview','Pass BUL intreview'),('Rejected by BUL','Rejected by BUL'),('Pass client intreview','Pass client intreview'),('Rejected by client','Rejected by client'),('Rejected pre-offer','Rejected pre-offer'),('Rejected offer','Rejected offer')]
    GROUP_OPTIONS = [('Autosar','Autosar'),('Business analyst','Business analyst'),('C/C++','C/C++'),('DevOps','DevOps'),('Frontend','Frontend'),('iOS','iOS'),('Java','Java'),('.NET','.NET'),('Python','Python'),('QA','QA')]
    FORMAT_OPTIONS = [('new','new'),('old','old')]
    CONTACT_OPTIONS = [('LinkedIn','LinkedIn'),('Referred','Referred'),('Applied on his own','Applied on his own'),('Phone','Phone'),('No info','No info'),] 

    name = models.CharField(max_length=200)
    recruiter = models.CharField(choices=RECRUITER_OPTIONS, max_length=200)
    contact_date = models.DateField()
    contact_mode = models.CharField(choices=CONTACT_OPTIONS, max_length=200, default="No info")
    technical_interview_date = models.DateField(default="2000-01-01")
    technical_interviewer = models.CharField(max_length=200,blank=True)
    technical_level = models.CharField(choices=LEVEL_OPTIONS,default='none', max_length=200, blank=True)
    bul_interview_date = models.DateField(default="2000-01-01")
    bul_interviewer = models.CharField(max_length=200, blank=True)
    group = models.CharField(choices=GROUP_OPTIONS, max_length=200)
    status = models.CharField(choices=STATUS_OPTIONS, max_length=200)
    technical_feedback = models.CharField( max_length=9999, default="no info")
    entry_format = models.CharField(choices=FORMAT_OPTIONS, max_length=200, default="old")
    # next_step = models.CharField(max_length=200)
    # created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name # this indicates the displayed value for each item under admin/questions ( text is a collumn of the table questions) 
    class Meta:
        verbose_name_plural = "Candidates" # this changes the plural from admin page avooiding double 's'