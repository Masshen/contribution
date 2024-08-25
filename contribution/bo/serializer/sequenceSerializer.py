from rest_framework import serializers
from bo.models import Sequences

class SequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sequences
        fields = '__all__'