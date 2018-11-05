from rest_framework import serializers
from .models import Client
from django.contrib.auth.models import User

 # (serializers.ModelSerializer):
 # (serializers.HyperlinkedModelSerializer):
class ClientSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Client
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    clients = serializers.PrimaryKeyRelatedField(many=True, queryset=Client.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'clients')