from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .serializers import ChoiceModelSerializer, PollModelSerializer
from .models import Choice, Poll


class ChoiceModelViewSet(ModelViewSet):
    serializer_class = ChoiceModelSerializer
    queryset = Choice.objects.all()

class PollModelViewSet(ModelViewSet):
    serializer_class = PollModelSerializer
    queryset = Poll.objects.all()