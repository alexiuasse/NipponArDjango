#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/08/2020 15:11.
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field
from django import forms

from .models import *


class IndividualCustomerForm(forms.ModelForm):
    layout = Layout(
        Div(
            Div(
                Field('name', wrapper_class='col-md-12'),
                Field('email', wrapper_class='col-md-12'),
                Field('phone', wrapper_class='col-md-12'),
                Field('cellphone', wrapper_class='col-md-12'),
                Field('cpf', wrapper_class='col-md-12'),
                css_class="col-md-6"
            ),
            Div(
                Field('street', wrapper_class='col-md-12'),
                Field('number', wrapper_class='col-md-12'),
                Field('neighborhood', wrapper_class='col-md-12'),
                Field('apartment', wrapper_class='col-md-12'),
                Field('block', wrapper_class='col-md-12'),
                Field('cep', wrapper_class='col-md-12'),
                Field('city', wrapper_class='col-md-12'),
                Field('state', wrapper_class='col-md-12'),
                # Field('address_line', wrapper_class='col-md-12'),
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
        self.helper.label_class = 'bmd-label-floating'

    class Meta:
        model = IndividualCustomer
        fields = ['name', 'email', 'phone',
                  'cpf', 'cellphone', 'street', 'number',
                  'neighborhood', 'apartment', 'block',
                  'city', 'state', 'cep', 'address_line']


class JuridicalCustomerForm(forms.ModelForm):
    layout = Layout(
        Div(
            Div(
                Field('name', wrapper_class='col-md-12'),
                Field('email', wrapper_class='col-md-12'),
                Field('phone', wrapper_class='col-md-12'),
                Field('cellphone', wrapper_class='col-md-12'),
                Field('cnpj', wrapper_class='col-md-12'),
                Field('parent_company', wrapper_class='col-md-12'),
                css_class='col-md-6'
            ),
            Div(
                Field('street', wrapper_class='col-md-12'),
                Field('number', wrapper_class='col-md-12'),
                Field('neighborhood', wrapper_class='col-md-12'),
                Field('apartment', wrapper_class='col-md-12'),
                Field('block', wrapper_class='col-md-12'),
                Field('cep', wrapper_class='col-md-12'),
                Field('city', wrapper_class='col-md-12'),
                Field('state', wrapper_class='col-md-12'),
                # Field('address_line', wrapper_class='col-md-12'),
                css_class="col-md-6"
            ),
            css_class='row'
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
        model = JuridicalCustomer
        fields = ['name', 'email', 'phone',
                  'cnpj',
                  'cellphone', 'street', 'number',
                  'neighborhood', 'apartment', 'block',
                  'city', 'state', 'cep',
                  'address_line', 'parent_company']
