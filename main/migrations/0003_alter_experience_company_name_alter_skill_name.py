# Generated by Django 4.2.3 on 2023-07-23 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
