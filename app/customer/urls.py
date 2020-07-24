#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/07/2020 15:54.
from django.urls import path

from .views import *

urlpatterns = [
    path('', CustomerView.as_view(), name='customer'),
    path('create/', CustomerCreate.as_view(), name='customer-create'),
    path('edit/<int:pk>/', CustomerEdit.as_view(), name='customer-edit'),
    path('del/<int:pk>/', CustomerDel.as_view(), name='customer-del'),
]
