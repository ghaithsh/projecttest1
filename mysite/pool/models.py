from django.contrib.gis.db import models

# Create your models here.


class club(models.Model):
    name = models.CharField(max_length=30)
    point = models.PointField(srid=4326)
