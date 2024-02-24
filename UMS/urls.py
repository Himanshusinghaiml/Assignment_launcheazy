from django.urls import path
from .views import UserSignupView
# from .views import *
from . import views
urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='user-signup'), 
    path('',views.org_name,name='orgname'),
    path('signup-page/',views.signupuser,name='signupuser'),
    path('login-page/',views.loginpage,name='loginpage'),
    path('user-login/', views.login_view, name='userlogin'),
    path('admin-dashboard/',views.admin_dash,name='admin-dash'),
    path('member-requests/',views.member,name='member'),
    
]
