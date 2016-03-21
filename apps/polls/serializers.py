from rest_framework import serializers
from . import models


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Poll
        # fields = ('id', 'account_name', 'users', 'created')
