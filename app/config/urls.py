#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 17/07/2020 19:36.

from django.urls import path

from .models_views.brand import *
from .models_views.model import *
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
]
