from django.contrib import admin
from cars.models import car, Brand 

class carAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')


class brandAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)


admin.site.register(Brand, brandAdmin)
admin.site.register(car, carAdmin)