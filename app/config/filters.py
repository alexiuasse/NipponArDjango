import django_filters
from .models import *

class BrandFilter(django_filters.FilterSet):

    class Meta:
        model = Brand
        fields = {'name':['icontains'],}
