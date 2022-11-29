from django.forms import ModelForm
from .models import JobApplication

class ApplyForm(ModelForm):
    class Meta:
        model = JobApplication
        fields = ['Job_Title','JobType','Full_Name','Email','PhoneNumber','Brief_introduction_about_yourself','Resume']
