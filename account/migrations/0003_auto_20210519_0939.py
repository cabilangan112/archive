# Generated by Django 3.1.4 on 2021-05-19 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210514_0603'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Dean',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='Faculty',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='Program_head',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='Students',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='quality_assurance',
            field=models.BooleanField(default=False),
        ),
    ]
