# Generated by Django 3.0.5 on 2020-11-09 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_user_diagnosis'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='disease_causes',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='disease',
            name='disease_description',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='disease',
            name='link',
            field=models.CharField(default='', max_length=500),
        ),
    ]
