# Generated by Django 4.2.3 on 2023-09-13 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='resume_certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certi_name', models.CharField(max_length=50)),
                ('certi_month', models.CharField(max_length=50)),
                ('certi_details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='resume_education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=50)),
                ('school_duration', models.CharField(max_length=50)),
                ('school_score', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='resume_projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('project_duration', models.CharField(max_length=50)),
                ('project_details', models.TextField()),
            ],
        ),
    ]
