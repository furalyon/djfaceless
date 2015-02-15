from django.contrib import admin
from . import models

class CardAdmin(admin.ModelAdmin):
    list_display = ('name','playerClass','type','rarity')
    search_fields = ('name','playerClass','type','race','faction')
    list_filter = ('playerClass','type','collectible','rarity')

admin.site.register(models.Card, CardAdmin)
admin.site.register(models.Mechanic)
admin.site.register(models.Type)
admin.site.register(models.Rarity)
admin.site.register(models.PlayerClass)
admin.site.register(models.Race)
admin.site.register(models.Faction)
admin.site.register(models.Set)