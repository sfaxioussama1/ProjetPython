from django.contrib import admin


from frontend.models import Contact
from frontend.models import Consultation
class ContactAdmin(admin.ModelAdmin):

    list_display = ('name','email','sujet','message')
    search_fields = ('name',)
class ConsultationAdmin(admin.ModelAdmin):

    list_display = ('name','prenom','date','time')
    search_fields = ('name',)
# Register your models here.
admin.site.register(Contact,ContactAdmin)
admin.site.register(Consultation,ConsultationAdmin)