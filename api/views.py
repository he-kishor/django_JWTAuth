from django.shortcuts import render

from .models import User,Profile
from .serlizers import UserSerilizers,TokenObtainPairSerializer,RegisterSerlizer

from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics,status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

class MyTokenobtainpPairView(TokenObtainPairView):
    serializer_class=TokenObtainPairSerializer

class Registrationview(generics.CreateAPIView):
    queryset=User.objects.all()
    permission_classes=(AllowAny,)
    serializer_class=RegisterSerlizer
    
    
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def dashbord(request):
    if request.method=="GET":
        response=f"Hey{request.user}, You are seeing the GET response"
        return Response(response, status=status.HTTP_200_OK)
    
    elif request.method=="POST":
        text=request.POST.get("text")
        response=f"Hey {request.user}, your text is {text}"
        return Response(response,status=status.HTTP_200_OK)
    
    return Response({}, status=status.HTTP_400_BAD_REQUEST)
        
    
        
        

        