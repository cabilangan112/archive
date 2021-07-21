# Generated by Django 3.1.4 on 2021-07-21 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('file', '0007_auto_20210714_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='memo',
            name='approve',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='memo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='memo',
            name='remove',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='memo',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='memo',
            name='content',
            field=models.FileField(null=True, upload_to='memo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='type_documents',
            field=models.CharField(blank=True, choices=[('Memorandum', 'Memorandum'), ('Research', 'Research'), ('Syllabus', 'Syllabus'), ('Curriculum', 'Curriculum')], default=True, max_length=30),
        ),
    ]
