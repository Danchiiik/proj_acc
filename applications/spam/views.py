from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from applications.spam.models import Spam

from applications.spam.serializers import SpamSerializer


class SpamApiView(ModelViewSet):
    queryset = Spam.objects.all()
    serializer_class = SpamSerializer
