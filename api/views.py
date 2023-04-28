from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import UserCreateSerializer, UserSerializer

# Routes
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/token',
        'api/token/refresh',
        'api/register',
        'api/curr'
    ]
    return Response(routes)

#User/Login/Register
@api_view(['POST'])
def registerUser(request):
    data = request.data

    serializer = UserCreateSerializer(data = data)
    if not serializer.is_valid():
        return Response(serializer.errors)
    
    user = serializer.create(serializer.validated_data)
    user = UserSerializer(user)

    return Response(user.data)

@api_view(['GET'])
def retrieveUser(request):
    user = request.user
    user = UserSerializer(user)

    return Response(user.data)