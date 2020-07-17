#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 17/07/2020 11:56.

from django.urls import path

from .views import *

urlpatterns = [
    path('brand/', BrandView.as_view(), name='config-brand'),
    path('brand/create/', BrandCreate.as_view(), name='config-brand-create'),
    path('brand/edit/<int:pk>/', BrandEdit.as_view(), name='config-brand-edit'),
    path('brand/del/<int:pk>/', BrandDel.as_view(), name='config-brand-del'),
]
