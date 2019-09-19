from django.db import models

# Create your models here.
class Parametre(models.Model):
    adresse=models.CharField(max_length=80)
    phone=models.CharField(max_length=20)
    email=models.EmailField()
    logo=models.FileField(upload_to='post_image',blank=True)
    def __str__(self):
        return self.adresse

class Docteur(models.Model):
    nom=models.CharField(max_length=20)
    prenom=models.CharField(max_length=20)
    description=models.CharField(max_length=80)
    specialite=models.CharField(max_length=20)
    image=models.FileField(upload_to='post_image',blank=True)
    def __str__(self):
        return self.nom

class Department(models.Model):
    nom=models.CharField(max_length=20)
    description=models.TextField()
    image=models.FileField(upload_to='post_image',blank=True)
    def __str__(self):
        return self.nom

class Prix(models.Model):
    type=models.CharField(max_length=20)
    prix=models.FloatField()
    service1=models.CharField(max_length=10,blank=True, null=True, default=' ')
    service2=models.CharField(max_length=10,blank=True, null=True, default=' ')
    service3=models.CharField(max_length=10,blank=True, null=True, default=' ')
    service4=models.CharField(max_length=10,blank=True, null=True, default=' ')
    def __str__(self):
        return self.type



class Apropos(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField()
    image=models.FileField(upload_to='post_image',blank=True)
    experience=models.IntegerField()
    nbrclient=models.IntegerField()
    nbrdoctor=models.IntegerField()
    nbrstaff=models.IntegerField()
    def __str__(self):
        return self.title













