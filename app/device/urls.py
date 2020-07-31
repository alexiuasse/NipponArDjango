#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 31/07/2020 10:18.
from django.urls import path

from .views import *

app_name = "device"

urlpatterns = [
    path('', DeviceIndex.as_view(), name='index'),
    path('view/', DeviceView.as_view(), name='view'),
    path('<int:cpk>/<int:ctp>/<int:pk>/profile/', DeviceProfile.as_view(), name='profile'),
    path('<int:cpk>/<int:ctp>/create/', DeviceCreate.as_view(), name='create'),
    path('<int:cpk>/<int:ctp>/<int:pk>/edit/', DeviceEdit.as_view(), name='edit'),
    path('<int:cpk>/<int:ctp>/<int:pk>/delete/', DeviceDel.as_view(), name='delete'),
]
