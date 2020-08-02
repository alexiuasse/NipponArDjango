#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 02/08/2020 10:07.

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('frontend.urls')),
    path('admin/', admin.site.urls),
    path('customer/', include('customer.urls')),
    path('config/', include('config.urls')),
    path('device/', include('device.urls')),
    path('service/', include('service.urls')),
]
