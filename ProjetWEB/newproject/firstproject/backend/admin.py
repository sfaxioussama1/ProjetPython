from django.contrib import admin
from backend.models import Parametre
from backend.models import Docteur
from backend.models import Department
from backend.models import Prix
from backend.models import Apropos

# Register your models here.
admin.site.register(Parametre)
admin.site.register(Docteur)
admin.site.register(Department)
admin.site.register(Prix)
admin.site.register(Apropos)