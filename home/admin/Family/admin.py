from django.contrib import admin
from ...models import *

class FamilyAdmin(admin.ModelAdmin):
    model = Family
    list_display = ('family_name',)
    search_fields = ('family_name',)

admin.site.register(Family, FamilyAdmin)  
