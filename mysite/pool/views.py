from django.shortcuts import render, HttpResponse
from .models import club
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D
# Create your views here.
strc = 'POINT (4 23)'


@api_view(['GET', 'POST'])
def addclub(request):
    b = club(name='Beatles Blog',
             point='POINT (33.52890763093399 36.2967423601667)')
    b.save()
    return Response({'massege': "done"})


@api_view(['GET', 'POST'])
def viewclub(request):
    lat = "33.50451303719481"
    long = "36.261084194427724"
    p = "POINT("+lat+" "+long+")"
    print(p)
    pnt = GEOSGeometry(p)
    print(club.objects.filter(point__distance_lte=(pnt, D(km=2))))
    return Response({'massege': "done"})
