from django.contrib import admin
from ...models import *


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('profile', 'event_name', 'event_date')
    search_fields = ('profile__user__username', 'event_name')
    list_filter = ('event_date',)