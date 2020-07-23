#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 22/07/2020 22:03.
from django.urls import path

from .views import *

urlpatterns = [
    path('', CustomerView.as_view(), name='customer'),
    path('create/', CustomerCreate.as_view(), name='customer-create'),
    path('edit/<int:pk>/', CustomerEdit.as_view(), name='customer-edit'),
    path('del/<int:pk>/', CustomerDel.as_view(), name='customer-del'),

    path('address/', CustomerAddressView.as_view(), name='customer-address'),
    path('address/create/', CustomerAddressCreate.as_view(), name='customer-address-create'),
    path('address/edit/<int:pk>/', CustomerAddressEdit.as_view(), name='customer-address-edit'),
    path('address/del/<int:pk>/', CustomerAddressDel.as_view(), name='customer-address-del'),
]
