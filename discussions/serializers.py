from discussions.models import *
from rest_framework import serializers

class discussSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'