#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 18/07/2020 12:09.

from django.urls import path

from .models_views.brand import *
from .models_views.model import *
from .models_views.type import *
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
]
