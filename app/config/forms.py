#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/07/2020 11:43.

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Column, Div, HTML
from django import forms

from .models import *


# REMEMBER: ALWAYS set the fields or the form will not save correctly.


class BaseConfigForm(forms.ModelForm):
    layout = Layout(
        Div(
            Column('name', css_class='form-group col-md'),
        ),
        Div(
            Column(
                HTML(
                    '<a href="{{ view.success_url }}" class="btn btn-danger btn-sm mr-2">Cancelar</a>'
                    '<button type="submit" class="btn btn-primary btn-sm">Finalizar</button>'),
                css_class='pull-right'
            ),
            css_class='row'
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_csrf = True
        self.helper = FormHelper()
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
