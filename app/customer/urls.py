#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 25/07/2020 22:44.
from django.urls import path

from .views import *

urlpatterns = [
    path('', Customer.as_view(), name='customer'),
    # individual customer
    path('individual', IndividualCustomerView.as_view(), name='customer-individual'),
    path('individual/create/', IndividualCustomerCreate.as_view(), name='customer-individual-create'),
    path('individual/edit/<int:pk>/', IndividualCustomerEdit.as_view(), name='customer-individual-edit'),
    path('individual/del/<int:pk>/', IndividualCustomerDel.as_view(), name='customer-individual-del'),
    # juridical customer
    path('juridical', JuridicalCustomerView.as_view(), name='customer-juridical'),
    path('juridical/create/', JuridicalCustomerCreate.as_view(), name='customer-juridical-create'),
    path('juridical/edit/<int:pk>/', JuridicalCustomerEdit.as_view(), name='customer-juridical-edit'),
    path('juridical/del/<int:pk>/', JuridicalCustomerDel.as_view(), name='customer-juridical-del'),
]
