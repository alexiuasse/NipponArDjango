#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 31/07/2020 14:27.
from django.urls import path, include

from .views import *

app_name = "customer"

individual_patterns = ([
                           path('', IndividualCustomerView.as_view(), name='view'),
                           path('create/', IndividualCustomerCreate.as_view(), name='create'),
                           path('<int:pk>/edit/', IndividualCustomerEdit.as_view(), name='edit'),
                           path('<int:pk>/del', IndividualCustomerDel.as_view(), name='delete'),
                       ], 'individualcustomer')

juridical_patterns = ([
                          path('', JuridicalCustomerView.as_view(), name='view'),
                          path('create/', JuridicalCustomerCreate.as_view(), name='create'),
                          path('<int:pk>/edit/', JuridicalCustomerEdit.as_view(), name='edit'),
                          path('<int:pk>/del', JuridicalCustomerDel.as_view(), name='delete'),
                      ], 'juridicalcustomer')

urlpatterns = [
    path('', Customer.as_view(), name='index'),
    path('profile/<int:pk>/<int:tp>/', CustomerProfile.as_view(), name='profile'),
    path('individual/', include(individual_patterns)),
    path('juridical/', include(juridical_patterns)),
]
