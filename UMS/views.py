from django.http import HttpResponse
from django.shortcuts import render
# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSignupSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSignupSerializer


@api_view(['POST'])
def user_signup(request):
    serializer = UserSignupSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'message': 'User signed up successfully.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def signupuser(req):
    return render(req,'singup.html')
 
class UserSignupView(APIView):
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  HttpResponse("successfully created user")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
