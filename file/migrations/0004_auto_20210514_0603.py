# Generated by Django 3.1.4 on 2021-05-14 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210514_0603'),
        ('file', '0003_auto_20210418_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.course'),
        ),
        migrations.AlterField(
            model_name='author',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.department'),
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
