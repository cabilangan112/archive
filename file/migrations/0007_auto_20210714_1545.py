# Generated by Django 3.1.4 on 2021-07-14 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0006_auto_20210520_0718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AddField(
            model_name='post',
            name='type_documents',
            field=models.CharField(blank=True, choices=[('1st', 'Firs Year'), ('2nd', 'Second Year'), ('3rd', 'Third Year'), ('4rt', 'Fourth Year'), ('grad', 'Graduate')], default=True, max_length=30),
        ),
    ]
