#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 22/07/2020 17:27.

from django.urls import path

from .models_views.brand import *
from .models_views.capacity import *
from .models_views.model import *
from .models_views.type import *
from .models_views.city import *
from .views import *

urlpatterns = [
    path('', Config.as_view(), name='config'),
    # brand url views
    path('brand/', BrandView.as_view(), name='config-brand'),
    path('brand/create/', BrandCreate.as_view(), name='config-brand-create'),
    path('brand/edit/<int:pk>/', BrandEdit.as_view(), name='config-brand-edit'),
    path('brand/del/<int:pk>/', BrandDel.as_view(), name='config-brand-del'),
    # model url views
    path('model/', ModelView.as_view(), name='config-model'),
    path('model/create/', ModelCreate.as_view(), name='config-model-create'),
    path('model/edit/<int:pk>/', ModelEdit.as_view(), name='config-model-edit'),
    path('model/del/<int:pk>/', ModelDel.as_view(), name='config-model-del'),
    # type url views
    path('type/', TypeView.as_view(), name='config-type'),
    path('type/create/', TypeCreate.as_view(), name='config-type-create'),
    path('type/edit/<int:pk>/', TypeEdit.as_view(), name='config-type-edit'),
    path('type/del/<int:pk>/', TypeDel.as_view(), name='config-type-del'),
    # capacity url views
    path('capacity/', CapacityView.as_view(), name='config-capacity'),
    path('capacity/create/', CapacityCreate.as_view(), name='config-capacity-create'),
    path('capacity/edit/<int:pk>/', CapacityEdit.as_view(), name='config-capacity-edit'),
    path('capacity/del/<int:pk>/', CapacityDel.as_view(), name='config-capacity-del'),
    # city url views
    path('city/', CityView.as_view(), name='config-city'),
    path('city/create/', CityCreate.as_view(), name='config-city-create'),
    path('city/edit/<int:pk>/', CityEdit.as_view(), name='config-city-edit'),
    path('city/del/<int:pk>/', CityDel.as_view(), name='config-city-del'),
]
