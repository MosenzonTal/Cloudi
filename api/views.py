from rest_framework import viewsets
from cloudinis.models import ActivatedPolicy, Violation
from .serializers import *


class ActivatedPolicyView(viewsets.ModelViewSet):
    queryset = ActivatedPolicy.objects.all()
    serializer_class = ActivatedPolicySerializer


class ViolationView(viewsets.ModelViewSet):
    queryset = Violation.objects.all()
    serializer_class = ViolationSerializer
