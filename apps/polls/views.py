from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import PollSerializer
from . import models
from rest_framework import viewsets
from rest_framework.response import Response
from django.views.generic import TemplateView


class PollViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PollSerializer
    queryset = models.Poll.objects.all()

class PollView(TemplateView):
    template_name = "poll.html"