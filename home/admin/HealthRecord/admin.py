from django.contrib import admin
from ...models import *

@admin.register(HealthRecord)
class HealthRecordAdmin(admin.ModelAdmin):
    list_display = ('profile', 'condition', 'doctor', 'date_recorded')
    search_fields = ('profile__user__username', 'condition')
    list_filter = ('date_recorded',)