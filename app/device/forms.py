#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 12/08/2020 15:40.
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Row, Div, Field
from django import forms

from .models import *


class DeviceForm(forms.ModelForm):
    layout = Layout(
        Div(
            Div(
                Field('identifier', wrapper_class='col-md-12'),
                Field('patrimony', wrapper_class='col-md-12'),
                Field('brand', wrapper_class='col-md-12'),
                Field('model', wrapper_class='col-md-12'),
                Field('type', wrapper_class='col-md-12'),
                Field('capacity', wrapper_class='col-md-12'),
                css_class="col-md-6"
            ),
            Div(
                Field('location', wrapper_class='col-md-12'),
                Field('observation', wrapper_class='col-md-12'),
                css_class="col-md-6"
            ),
            css_class="row"
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_csrf = True
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = self.layout
        self.helper.form_class = 'form-control'
        # self.helper.label_class = 'bmd-label-floating'

    class Meta:
        model = Device
        # widgets = {
        #     'location': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        #     'observation': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        # }
        fields = ['identifier', 'patrimony', 'observation', 'location',
                  'brand', 'model', 'type', 'capacity', ]
