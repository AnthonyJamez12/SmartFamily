from django.contrib import admin
from ...models import *

class ProfileInline(admin.TabularInline):
    model = Profile
    fields = ('user', 'first_name', 'last_name', 'role', 'birth_date', 'gender')
    extra = 0  # Do not show extra empty rows

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('user', 'first_name', 'last_name', 'birth_date', 'gender', 'get_family_name')
    search_fields = ('user__username', 'first_name', 'last_name')
    list_filter = ('gender', 'family')
    fieldsets = (
        ('User Info', {'fields': ('user',)}),
        ('Profile Details', {'fields': ('first_name', 'last_name', 'birth_date', 'gender', 'role', 'family')}),
    )

    def get_family_name(self, obj):
        """Show the family name associated with this profile."""
        return obj.family.family_name if obj.family else "No Family"
    get_family_name.short_description = 'Family'

# Register the modified admin models
admin.site.register(Profile, ProfileAdmin)