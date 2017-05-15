from django.contrib import admin
from .models import Population, Suco, Aldeia

class PopulationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Population, PopulationAdmin)


class SucoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Suco, SucoAdmin)


class AldeiaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Aldeia, AldeiaAdmin)
