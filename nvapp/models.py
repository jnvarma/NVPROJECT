from django.db import models

class PythonApplication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    education_type = models.CharField(max_length=20, choices=[
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('doctorate', 'Doctorate'),
        ('others', 'Others')
    ])
    year_started = models.DateField()
    year_passed = models.DateField()
    skills = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()

class JavaApplication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    education_type = models.CharField(max_length=20, choices=[
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('doctorate', 'Doctorate'),
        ('others', 'Others')
    ])
    year_started = models.DateField()
    year_passed = models.DateField()
    skills = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    

class AssApplication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    education_type = models.CharField(max_length=20, choices=[
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('doctorate', 'Doctorate'),
        ('others', 'Others')
    ])
    year_started = models.DateField()
    year_passed = models.DateField()
    skills = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()

class CoordinatorApplication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    education_type = models.CharField(max_length=20, choices=[
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('doctorate', 'Doctorate'),
        ('others', 'Others')
    ])
    year_started = models.DateField()
    year_passed = models.DateField()
    skills = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    
class JavafullApplication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    education_type = models.CharField(max_length=20, choices=[
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('doctorate', 'Doctorate'),
        ('others', 'Others')
    ])
    year_started = models.DateField()
    year_passed = models.DateField()
    skills = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    
class PythonfullApplication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    education_type = models.CharField(max_length=20, choices=[
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('doctorate', 'Doctorate'),
        ('others', 'Others')
    ])
    year_started = models.DateField()
    year_passed = models.DateField()
    skills = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()

    
