from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('brand/', BrandView.as_view(), name='config-brand'),
    path('brand/create/', BrandCreate.as_view(), name='config-brand-create'),
    path('brand/edit/<int:pk>/', BrandEdit.as_view(), name='config-brand-edit'),
    path('brand/del/<int:pk>/', BrandDel.as_view(), name='config-brand-del'),
]
