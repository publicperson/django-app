# Generated by Django 4.1.3 on 2022-11-25 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_alter_joblist_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblist',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
