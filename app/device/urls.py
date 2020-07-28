#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 28/07/2020 08:55.
from django.urls import path

from .views import *

urlpatterns = [
    path('', DeviceIndex.as_view(), name='device'),
    # device
    path('device', DeviceView.as_view(), name='device-view'),
    path('device/create/', DeviceCreate.as_view(), name='device-create'),
    path('device/edit/<int:pk>/', DeviceEdit.as_view(), name='device-edit'),
    path('device/del/<int:pk>/', DeviceDel.as_view(), name='device-del'),
]
