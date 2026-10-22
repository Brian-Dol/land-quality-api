from rest_framework import serializers
from .models import Owner, Land, LandQualityAssessment

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

class LandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = '__all__'

class LandQualityAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandQualityAssessment
        fields = '__all__'
