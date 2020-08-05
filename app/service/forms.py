#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 05/08/2020 19:00.
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Row, Div, Field
from django import forms

from .models import *


class OrderOfServiceForm(forms.ModelForm):
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
                            Field('type_of_service', wrapper_class='col-md-12'),
                            Field('status', wrapper_class='col-md-12'),
                            Field('parts', wrapper_class='col-md-12'),
                            Field('start_date', wrapper_class='col-md-12'),
                            Field('end_date', wrapper_class='col-md-12'),
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
                            Field('scheduled', wrapper_class='col-md-12'),
                            Field('defect', wrapper_class='col-md-12'),
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
        # self.helper.label_class = 'bmd-label-floating'

    class Meta:
        model = OrderOfService
        widgets = {
            'start_date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'end_date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
        fields = ['type_of_service', 'status',
                  'parts', 'start_date', 'end_date',
                  'defect', 'observation', 'scheduled']
