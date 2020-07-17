#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 09/07/2020 10:07.

from django.urls import path
from django.contrib.auth import views as auth_views
from frontend.views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('user/', User.as_view(), name='user'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('home/', Home.as_view(), name='home'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('icons/', Icons.as_view(), name='icons'),
    path('tables/', Tables.as_view(), name='tables'),
    path('typography/', Typography.as_view(), name='typography'),
    path('maps/', Maps.as_view(), name='maps'),
    path('notifications/', Notifications.as_view(), name='notifications'),
]
