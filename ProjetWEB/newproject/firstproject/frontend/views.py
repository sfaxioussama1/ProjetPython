from django.shortcuts import render
from .forms import ContactCreate
from .forms import ConsultationCreate
from frontend import models
from backend import models
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.
def Index(request):
    apropos=models.Apropos.objects.all()
    docteurs=models.Docteur.objects.all()
    departements=models.Department.objects.all()
    prixs=models.Prix.objects.all()
    form=ConsultationCreate(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Votre message est envoyé avec succès")
        return HttpResponseRedirect('/')
    context={
            'apropos':apropos,
            'docteurs':docteurs,
            'departements':departements,
            'prixs':prixs,
            'form':form

         }
    return render(request,'index.html',context)

def Docteur(request):
    docteurs=models.Docteur.objects.all()
    context={
        'docteurs':docteurs
    }
    return render(request,'Docteur.html',context)
def Contact(request):
    form=ContactCreate(request.POST )
    if form.is_valid():
        form.save()
        messages.success(request,"Votre message est envoyé avec succès")
        return HttpResponseRedirect('/contact/')

    parametres=models.Parametre.objects.all()


    context={
        'parametres':parametres,
        'form':form
        }

    return render(request,'contact.html',context)

def Departement(request):
    departements=models.Department.objects.all()
    context={
        'departements':departements
    }
    return render(request,'departement.html',context)

def Prix(request):
    prixs=models.Prix.objects.all()
    context={
        'prixs':prixs
     }

    return render(request,'prix.html',context)


def Apropo(request):
    apropos=models.Apropos.objects.all()
    context={
            'apropos':apropos
         }
    return render(request,'About.html',context)
