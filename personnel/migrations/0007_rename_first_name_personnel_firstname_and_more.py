# Generated by Django 4.1.3 on 2022-11-23 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0006_rename_university_education_institution_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personnel',
            old_name='First_Name',
            new_name='FirstName',
        ),
        migrations.RenameField(
            model_name='personnel',
            old_name='Last_Name',
            new_name='LastName',
        ),
    ]
