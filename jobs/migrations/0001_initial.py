# Generated by Django 4.1.3 on 2022-11-23 20:27

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=300)),
                ('Email', models.EmailField(max_length=254)),
                ('PhoneNumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('Brief_introduction_about_yourself', models.TextField()),
                ('Resume', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='JobList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=258)),
                ('Description', models.TextField()),
                ('Required_Skills', models.TextField()),
                ('Salary', models.TextField(blank=True)),
                ('Location', models.CharField(max_length=400)),
            ],
        ),
    ]
