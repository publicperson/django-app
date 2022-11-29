from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from ckeditor.fields import RichTextField
import uuid
# Create your models here.


class JobList(models.Model):
    Title = models.CharField(max_length=258)
    Type = models.CharField(max_length=200, blank=True)
    Description = models.TextField()
    Required_Skills = RichTextField()
    Salary = models.TextField(blank=True)
    Location = models.CharField(max_length=400)
    
    
    def __str__(self):
        return self.Title



class JobApplication(models.Model):
    Job_Title = models.ForeignKey(JobList,on_delete=models.DO_NOTHING,null=True)
    class Job_Type(models.TextChoices):
        Part_Time = 'Part-Time'
        Full_Time = 'Full-Time'
        Contract = 'Contract'
        Intern = 'Intern'
        National_Service = 'National Service'
        
    JobType = models.CharField(max_length=24,choices=Job_Type.choices,blank=True,default=Job_Type.Part_Time)
    Full_Name = models.CharField(max_length=300)
    Email = models.EmailField()
    PhoneNumber = PhoneNumberField()
    Brief_introduction_about_yourself = models.TextField()
    Resume = models.FileField(null=True)
    
    
        
    def __str__(self):
        return self.Full_Name
    