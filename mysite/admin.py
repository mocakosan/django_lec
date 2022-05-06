from django.contrib import admin
from .models import MainContent
from .models import Notices

admin.site.register(MainContent)
# Register your models here.
admin.site.register(Notices)