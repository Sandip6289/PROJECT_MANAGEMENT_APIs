from rest_framework import serializers
from rest_framework import status
from .models import User, EmpA, EmpS

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email', 'password','role')


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, required=True)
    
    class Meta:
        model = User
        fields = ['email', 'password']


class EmpADetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpA
        fields = "__all__"
        depth = 1

class EmpSDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpS
        fields = "__all__"
        depth = 1