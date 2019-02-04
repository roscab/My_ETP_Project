from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Candidate

class NewCandidate(forms.ModelForm):

    class Meta:
        model = Candidate  
        fields = ('name','email','phone','skype','contact_date','contact_mode','recruiter','group')
    
    def __init__(self, *args, **kwargs):
        super(NewCandidate, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'John Doe'
        self.fields['email'].widget.attrs['placeholder'] = 'john_doe@gmail.com'
        self.fields['phone'].widget.attrs['placeholder'] = '+34123456789'
        self.fields['skype'].widget.attrs['placeholder'] = 'johnDoe2018'
        self.fields['contact_date'].widget.attrs['placeholder'] = '2018-10-30'
    
class NewStatus(forms.ModelForm):

    class Meta:
        model = Candidate  
        fields = ("status",)

class NewTechReport(forms.ModelForm):

    class Meta:
        model = Candidate  
        widgets = {'technical_feedback': forms.Textarea,}
        fields = ('technical_interviewer','technical_level','technical_interview_date','technical_feedback')

    def __init__(self, *args, **kwargs):
        super(NewTechReport, self).__init__(*args, **kwargs)
        self.fields['technical_interview_date'].widget.attrs['placeholder'] = '2018-10-30'
        self.fields['technical_feedback'].widget.attrs['placeholder'] = 'Write your feedback here'

class NewBulReport(forms.ModelForm):

    class Meta:
        model = Candidate  
        widgets = {'technical_feedback': forms.Textarea, 'bul_feedback': forms.Textarea, }
        fields = ('bul_interviewer','bul_interview_date','bul_verdic','bul_feedback')
    def __init__(self, *args, **kwargs):
        super(NewBulReport, self).__init__(*args, **kwargs)
        self.fields['bul_interview_date'].widget.attrs['placeholder'] = '2018-10-30'
        self.fields['bul_feedback'].widget.attrs['placeholder'] = 'Write your feedback here'
