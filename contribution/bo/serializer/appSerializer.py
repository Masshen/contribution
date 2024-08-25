from rest_framework import serializers
from bo.models import Apps

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apps
        fields = '__all__'