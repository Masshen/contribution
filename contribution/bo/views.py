from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from .serializer.mediaSerializer import MediaSerializer
from .serializer.appSerializer import AppSerializer
from .serializer.languageSerializer import LanguageSerializer
from .serializer.sequenceSerializer import SequenceSerializer
from .models import Medias


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Medias.objects.all()
    serializer_class = MediaSerializer
    def post(self,request,format=None):
        return Response({'received data': request.data})
class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Medias.objects.all()
    serializer_class = LanguageSerializer
class SequenceViewSet(viewsets.ModelViewSet):
    queryset = Medias.objects.all()
    serializer_class = SequenceSerializer
class AppViewSet(viewsets.ModelViewSet):
    queryset = Medias.objects.all()
    serializer_class = AppSerializer

def home(request):
    return HttpResponse("<H1>MASS</H1>")
