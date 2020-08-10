#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 10/08/2020 10:15.

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field
from django import forms

from .models import *


# REMEMBER: ALWAYS set the fields or the form will not save correctly.


class BaseConfigForm(forms.ModelForm):
    layout = Layout(
        Row(
            Field('name', wrapper_class='col-md-12'),
            Field('contextual', wrapper_class='col-md-12'),
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_csrf = True
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = self.layout
        self.helper.form_class = 'form-control'
        self.helper.label_class = 'bmd-label-floating'


class BrandForm(BaseConfigForm):
    class Meta:
        model = Brand
        fields = ['name']


class ModelForm(BaseConfigForm):
    class Meta:
        model = Model
        fields = ['name']


class TypeForm(BaseConfigForm):
    class Meta:
        model = Type
        fields = ['name']


class CapacityForm(BaseConfigForm):
    class Meta:
        model = Capacity
        fields = ['name']


class CityForm(BaseConfigForm):
    class Meta:
        model = City
        fields = ['name']


class TypeOfServiceForm(BaseConfigForm):
    class Meta:
        model = TypeOfService
        fields = ['name']


class StatusServiceForm(BaseConfigForm):
    class Meta:
        model = StatusService
        fields = ['name', 'contextual']


class DevicePartsForm(BaseConfigForm):
    class Meta:
        model = DeviceParts
        fields = ['name']
