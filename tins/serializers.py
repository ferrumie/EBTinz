from rest_framework import serializers
from .models import Tins
from django.conf import settings
class TinSerializer(serializers.ModelSerializer):
    
