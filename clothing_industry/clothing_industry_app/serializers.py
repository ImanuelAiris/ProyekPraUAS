from rest_framework import serializers
from .models import *
    
class Sistem1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sistem1
        fields = "__all__"

class Sistem2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sistem2
        fields = "__all__"

class Sistem3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sistem3
        fields = "__all__"

class Sistem4Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sistem4
        fields = "__all__"

class Sistem5Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sistem5
        fields = "__all__"

class Sistem6Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sistem6
        fields = "__all__"

class Sistem7Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sistem7
        fields = "__all__"

class Sistem8Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sistem8
        fields = "__all__"

class Sistem9Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sistem9
        fields = "__all__"

class AktuatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aktuator
        fields = "__all__"
        