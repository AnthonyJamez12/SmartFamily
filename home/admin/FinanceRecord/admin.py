from django.contrib import admin
from ...models import *


@admin.register(FinanceRecord)
class FinanceRecordAdmin(admin.ModelAdmin):
    list_display = ('profile', 'transaction', 'amount', 'date')
    search_fields = ('profile__user__username', 'transaction')
    list_filter = ('date', 'amount')