from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=80)
    email=models.EmailField(max_length=80)
    sujet=models.CharField(max_length=80)
    message=models.TextField()
    def __str__(self):
        return self.name
class Consultation(models.Model):
    name=models.CharField(max_length=80)
    prenom=models.CharField(max_length=80)
    date=models.DateField()
    time=models.TimeField()
    message=models.TextField()
    def __str__(self):
        return self.name