from rest_framework import serializers
from bo.models import Medias

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medias
        fields = '__all__'