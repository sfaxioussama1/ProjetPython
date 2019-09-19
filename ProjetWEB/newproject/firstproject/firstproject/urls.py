"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from frontend.views import Index
from frontend.views import Docteur
from frontend.views import Contact
from frontend.views import Departement
from frontend.views import Prix
from frontend.views import Apropo
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header= 'Tounsi Clinique'
admin.site.site_title=  'Tounsi Clinique'
admin.site.index_title= 'Dashboard Admin Tounsi Clinique'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index,name='index'),
    path('docteur/',Docteur,name='docteur'),
    path('contact/',Contact,name='contact'),
    path('departement/',Departement,name='departement'),
    path('prix/',Prix,name='prix'),
    path('apropos/',Apropo,name='Apropo'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
