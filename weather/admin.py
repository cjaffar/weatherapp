from django.contrib import admin

from .models import Weather, City


class WeatherAdmin(admin.ModelAdmin):
    list_display = ('city','date','min_temp','max_temp','rain',)


class CityAdmin(admin.ModelAdmin):
    list_display=('name','cityid','status','country',)


admin.site.register(Weather, WeatherAdmin)
admin.site.register(City, CityAdmin)
