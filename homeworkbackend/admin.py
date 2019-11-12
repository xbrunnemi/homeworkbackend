from django.contrib import admin

# Register your models here.
from swengs.homeworkbackend import models


class SoldierAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'arm_of_service', 'country')
    search_fields = (['first_name', 'last_name'])
    sortable_by = (['last_name', 'arm_of_service', 'country'])
    list_filter = (['last_name'])


class CountryAdmin(admin.ModelAdmin):
    list_display = (['name'])


admin.site.register(models.Soldier, SoldierAdmin)

admin.site.register(models.Country, CountryAdmin)