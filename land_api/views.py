from rest_framework import viewsets, permissions
from .models import Owner, Land, LandQualityAssessment
from .serializers import OwnerSerializer, LandSerializer, LandQualityAssessmentSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = [permissions.IsAuthenticated]  # Require authentication

class LandViewSet(viewsets.ModelViewSet):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
    permission_classes = [permissions.IsAuthenticated]  # Require authentication

class LandQualityAssessmentViewSet(viewsets.ModelViewSet):
    queryset = LandQualityAssessment.objects.all()
    serializer_class = LandQualityAssessmentSerializer
    permission_classes = [permissions.IsAuthenticated]  # Require authentication
