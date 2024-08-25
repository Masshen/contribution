from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser,MultiPartParser
from .serializer.mediaSerializer import MediaSerializer
from .serializer.appSerializer import AppSerializer
from .serializer.languageSerializer import LanguageSerializer
from .serializer.sequenceSerializer import SequenceSerializer
from .models import Medias


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Medias.objects.all()
    serializer_class = MediaSerializer
    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            #return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            print("Errors:", serializer.errors)
            #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
