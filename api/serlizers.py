from rest_framework_simplejwt.tokens import Token
from  models import User, Profile
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class UserSerilizers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email']
        
class TokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token= super().get_token(user)