#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 31/07/2020 14:42.

from django.urls import path, include

from .views import *

app_name = "config"

brand_patterns = ([
                      path('', BrandView.as_view(), name='view'),
                      path('create/', BrandCreate.as_view(), name='create'),
                      path('<int:pk>/edit/', BrandEdit.as_view(), name='edit'),
                      path('<int:pk>/del', BrandDel.as_view(), name='delete'),
                  ], 'brand')
model_patterns = ([
                      path('', ModelView.as_view(), name='view'),
                      path('create/', ModelCreate.as_view(), name='create'),
                      path('<int:pk>/edit/', ModelEdit.as_view(), name='edit'),
                      path('<int:pk>/del', ModelDel.as_view(), name='delete'),
                  ], 'model')
type_patterns = ([
                     path('', TypeView.as_view(), name='view'),
                     path('create/', TypeCreate.as_view(), name='create'),
                     path('<int:pk>/edit/', TypeEdit.as_view(), name='edit'),
                     path('<int:pk>/del', TypeDel.as_view(), name='delete'),
                 ], 'type')
capacity_patterns = ([
                         path('', CapacityView.as_view(), name='view'),
                         path('create/', CapacityCreate.as_view(), name='create'),
                         path('<int:pk>/edit/', CapacityEdit.as_view(), name='edit'),
                         path('<int:pk>/del', CapacityDel.as_view(), name='delete'),
                     ], 'capacity')
city_patterns = ([
                     path('', CityView.as_view(), name='view'),
                     path('create/', CityCreate.as_view(), name='create'),
                     path('<int:pk>/edit/', CityEdit.as_view(), name='edit'),
                     path('<int:pk>/del', CityDel.as_view(), name='delete'),
                 ], 'city')
urlpatterns = [
    path('', Config.as_view(), name='index'),
    path('brand/', include(brand_patterns)),
    path('model/', include(model_patterns)),
    path('type/', include(type_patterns)),
    path('capacity/', include(capacity_patterns)),
    path('city/', include(city_patterns)),
]
