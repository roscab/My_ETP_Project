from django import forms
from .models import Candidate

class NewCandidate(forms.ModelForm):

    class Meta:
        model = Candidate     
        fields = ('name','email','phone','skype','contact_date','contact_mode','recruiter','group')