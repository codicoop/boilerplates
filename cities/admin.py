from django.contrib import admin

from .models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'county', 'province', 'postal_code',
    )
    list_filter = ('county', 'province')
    search_fields = (
        'name__unaccent', 'postal_code',
    )
    ordering = ('name_order',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
