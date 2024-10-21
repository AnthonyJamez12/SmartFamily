from django.contrib import admin
from ...models import *

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'teacher', 'grade')
    search_fields = ('class_name',)
    list_filter = ('grade',)