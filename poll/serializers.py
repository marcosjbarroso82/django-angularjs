
from rest_framework import serializers


from .models import Poll, Choice



class ChoiceModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice


class PollModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll