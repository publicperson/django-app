from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from sorl.thumbnail import ImageField

# Create your models here.

class Personnel(models.Model):
    FirstName = models.CharField(max_length=130)
    LastName = models.CharField(max_length=130)
    Other_Names = models.CharField(max_length=130, blank='yes')
    Email = models.EmailField()
    Gender = models.CharField(max_length=200, blank=True)
    Contact = PhoneNumberField(blank=True)
    Address = models.CharField(max_length=130)
    Summary = models.TextField()
    Status = models.CharField(max_length=130, blank='yes')
    Project = models.ManyToManyField('Project')
    Education = models.ManyToManyField('Education')
    Experience = models.ManyToManyField('Experience')
    Skill = models.ManyToManyField('Skill',)
    Profile_Picture = ImageField()
    
    def __str__(self):
        return u'%s %s' %(self.FirstName, self.LastName)
    
class Education(models.Model):
    Programme = models.CharField(max_length=200)
    Institution = models.CharField(max_length=300)
    Start_Date = models.DateField()
    End_Date = models.DateField(blank=True)
    
    def __str__(self):
        return self.Programme
    
    
class Experience(models.Model):
    Start_Date = models.DateField()
    End_Date = models.DateField( blank=True)
    Role = models.CharField(max_length=250)
    Company = models.CharField(max_length=300)
    Task = models.TextField()
    
    def __str__(self):
        return self.Company
    
    
class Skill(models.Model):
    Title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Title
    
class Project(models.Model):
    Title = models.CharField(max_length=300)
    Link = models.URLField()
    Link_Name = models.CharField(max_length=100, blank='yes')
    Description =  models.TextField(blank=True)
    Contribution = models.TextField(blank=True)
    Start_Date = models.DateField()
    End_Date = models.DateField()
    ScreenShot = ImageField()
    ScreenShot1 = ImageField(blank=True)
    ScreenShot2 = ImageField(blank=True)
    
    def __str__(self):
        return self.Title
    
    