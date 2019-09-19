from django import forms
from .models import Contact
from .models import Consultation
class ContactCreate(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Saisir Votre Nom'
        }
    )
    )

    email=forms.EmailField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Saisir Votre Email'

        }
    )
    )

    sujet=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Saisir Votre Sujet'
        }
    ))
    message=forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder':'Saisir Votre Message'
        }
    )
    )

    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'sujet',
            'message'
        ]

class ConsultationCreate(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Saisir Votre Nom'
        }
    )
    )

    prenom=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Saisir Votre prenom'

        }
    )
    )



    date=forms.DateField(widget=forms.TextInput(
        attrs={
            'class':'form-control appointment_date',
            'placeholder':'Saisir Votre Date'
        }
    ))

    time=forms.TimeField(widget=forms.TextInput(
        attrs={
            'class':'form-control appointment_time',
            'placeholder':'Saisir Time'
        }
    ))
    message=forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder':'Saisir Votre Message'
        }
    )
    )

    class Meta:
        model = Consultation
        fields = [
            'name',
            'prenom',
            'date',
            'time',
            'message'
        ]