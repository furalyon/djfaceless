from django.contrib import admin
from . import models

class CardAdmin(admin.ModelAdmin):
    list_display = ('name','playerClass','type')
    search_fields = ('name','playerClass','type','race','faction')
    list_filter = ('playerClass','type')

admin.site.register(models.Card, CardAdmin)
admin.site.register(models.Mechanic)