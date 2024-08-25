from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializer.mediaSerializer import MediaSerializer
from .models import Medias


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Medias.objects.all()
    serializer_class = MediaSerializer

def home(request):
    return HttpResponse("<H1>MASS</H1>")
