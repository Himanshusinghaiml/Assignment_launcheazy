from django.urls import path
from .views import UserSignupView
# from .views import *
from . import views
urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='user-signup'),
    path('',views.signupuser,name='sign')
    
]
