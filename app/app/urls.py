#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 15/08/2020 15:46.

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

# Handling errors, but only if debug is set to False and there is another server to serve staticfiles
handler400 = 'frontend.views.error_400'
handler401 = 'frontend.views.error_401'
handler403 = 'frontend.views.error_403'
handler404 = 'frontend.views.error_404'
handler500 = 'frontend.views.error_500'
handler503 = 'frontend.views.error_503'
