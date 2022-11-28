# Generated by Django 4.1.3 on 2022-11-25 17:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_alter_joblist_required_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblist',
            name='id',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]