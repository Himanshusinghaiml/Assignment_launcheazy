from django.http import HttpResponse
from django.shortcuts import redirect, render
# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSignupSerializer
from django.contrib.auth import authenticate, login
 
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
    return render(req,'signup.html')

def org_name(req):
    return render(req,'org_name.html')

class UserSignupView(APIView):
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  redirect('login-page')
        return  redirect('signupuser')


def loginpage(req):
    return render(req,'login.html')

 
def admin_dash(req):
    return render(req,'admin_dash.html')

from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin-dash')  # Redirect to the dashboard page after successful login
        else:
            # Authentication failed
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
def member(req):
    return render(req,'member-req.html')