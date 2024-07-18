from rest_framework_simplejwt.tokens import Token
from .models import User, Profile
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
        
        token['Full_name']=user.profile.full_name
        token['username']=user.username
        token['email']=user.email
        token['bio']=user.profile.bio 
        token['image']=str(user.profile.image)
        token['verified']=user.profile.verified
        
        return token
class RegisterSerlizer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2=serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model=User
        fields=['email','username','password','password2']
        
        
    def validate(self, attrs):
        if attrs['password']!=attrs['password2']:
            raise serializers.ValidationError({"password":"password fields does not match"}) 
        return attrs
    
    def create(self,attrs):
        user=User.objects.create(
            username=attrs['username'],    
            email=attrs['email'],
            
        )
        user.set_password(attrs['password'])
        user.save()
        return user
        