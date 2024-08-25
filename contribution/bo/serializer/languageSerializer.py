from rest_framework import serializers
from bo.models import Languages

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = '__all__'