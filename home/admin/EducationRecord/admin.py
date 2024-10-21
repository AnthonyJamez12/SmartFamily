from django.contrib import admin
from ...models import *


@admin.register(EducationRecord)
class EducationRecordAdmin(admin.ModelAdmin):
    list_display = ('profile', 'school', 'class_record', 'date_started')
    search_fields = ('profile__user__username', 'school')
    list_filter = ('date_started',)