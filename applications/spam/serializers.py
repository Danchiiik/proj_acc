from rest_framework import serializers

from applications.spam.models import Spam

class SpamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spam
        fields = '__all__'
        
