# Generated by Django 4.2.3 on 2023-08-12 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nvapp', '0002_javaapplication'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('education_type', models.CharField(choices=[('bachelor', 'Bachelor'), ('master', 'Master'), ('doctorate', 'Doctorate'), ('others', 'Others')], max_length=20)),
                ('year_started', models.DateField()),
                ('year_passed', models.DateField()),
                ('skills', models.TextField()),
                ('resume', models.FileField(upload_to='resumes/')),
                ('cover_letter', models.TextField()),
            ],
        ),
    ]