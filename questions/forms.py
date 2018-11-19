from django import forms
from .models import Candidate

class NewCandidate(forms.ModelForm):

    class Meta:
        model = Candidate  
        fields = ('name','email','phone','skype','contact_date','contact_mode','recruiter','group','technical_interviewer')
    
    def __init__(self, *args, **kwargs):
        super(NewCandidate, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'John Doe'
        self.fields['email'].widget.attrs['placeholder'] = 'john_doe@gmail.com'
        self.fields['phone'].widget.attrs['placeholder'] = '+34123456789'
        self.fields['skype'].widget.attrs['placeholder'] = 'johnDoe2018'
        self.fields['contact_date'].widget.attrs['placeholder'] = '2018-10-30'

        


