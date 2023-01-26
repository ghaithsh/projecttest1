from django.contrib.gis import admin
from .models import club
# Register your models here.
admin.site.register(club, admin.OSMGeoAdmin)
