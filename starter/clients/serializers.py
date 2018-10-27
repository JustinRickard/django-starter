from rest_framework import serializers
from .models import Client

 # (serializers.ModelSerializer):
 # (serializers.HyperlinkedModelSerializer):
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'