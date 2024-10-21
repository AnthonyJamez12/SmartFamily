from django.contrib import admin
from ...models import *

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'specialty')
    search_fields = ('name', 'location') 