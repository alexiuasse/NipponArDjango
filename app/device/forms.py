#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 28/07/2020 10:04.
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Row, Div, Field
from django import forms

from .models import *


class DeviceForm(forms.ModelForm):
    layout = Layout(
        Div(
            Div(
                Div(
                    Div(
                        HTML('<h6 class="card-title">Descrição do Equipamento</h6>'),
                        css_class='card-header'
                    ),
                    Div(
                        Row(
                            Field('name', wrapper_class='col-md-12'),
                            Field('patrimony', wrapper_class='col-md-12'),
                            Field('brand', wrapper_class='col-md-12'),
                            Field('model', wrapper_class='col-md-12'),
                            Field('type', wrapper_class='col-md-12'),
                            Field('capacity', wrapper_class='col-md-12'),
                        ),
                        css_class='card-body'
                    ),
                    css_class='card'
                ),
                css_class='col-md-6'
            ),
            Div(
                Div(
                    Div(
                        HTML('<h6 class="card-title">Dados do Equipamento</h6>'),
                        css_class='card-header'
                    ),
                    Div(
                        Row(
                            Field('entry_date', wrapper_class='col-md-12'),
                            Field('departure_date', wrapper_class='col-md-12'),
                            Field('location', wrapper_class='col-md-12'),
                            Field('observation', wrapper_class='col-md-12'),
                        ),
                        css_class='card-body'
                    ),
                    css_class='card'
                ),
                css_class='col-md-6'
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
        self.helper.label_class = 'bmd-label-floating'

    class Meta:
        model = Device
        fields = ['name', 'patrimony', 'entry_date',
                  'departure_date', 'observation', 'location',
                  'brand', 'model', 'type', 'capacity', ]
