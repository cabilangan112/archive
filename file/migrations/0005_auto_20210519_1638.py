# Generated by Django 3.1.4 on 2021-05-19 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0004_auto_20210514_0603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.FileField(null=True, upload_to='content')),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_uploaded'],
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='date_modified',
        ),
    ]