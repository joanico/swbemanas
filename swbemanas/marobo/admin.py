from django.contrib import admin
from .models import Population

class PopulationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Population, PopulationAdmin)
