from django.urls import path
from django.contrib.auth import views as auth_views
from frontend.views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('user/', User.as_view(), name='user'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('home/', Home.as_view(), name='home'),
]
