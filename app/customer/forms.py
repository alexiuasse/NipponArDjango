#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 22/07/2020 22:53.
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Column, Div, HTML, Row
from django import forms

from .models import *


class CustomerForm(forms.ModelForm):
    layout = Layout(
        'name',
        'email',
        Row(
            Column('phone_1', css_class='col-md-6'),
            Column('phone_2', css_class='col-md-6'),
        ),
        Row(
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

    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone_1', 'phone_2']


class CustomerAddressForm(forms.ModelForm):
    layout = Layout(
        # Row(
        #     Column('customer', css_class='col-md'),
        #     Column('street', css_class='col-md'),
        #     Column('number', css_class='col-md'),
        #     Column('city', css_class='col-md'),
        #     Column('state', css_class='col-md'),
        #     Column('cep', css_class='col-md'),
        #     Column('address_line', css_class='col-md'),
        # ),
        'customer',
        Row(
            Column('street', css_class='col-md-4'),
            Column('number', css_class='col-md-4'),
            Column('cep', css_class='col-md-4'),
        ),
        Row(
            Column('city', css_class='col-md-6'),
            Column('state', css_class='col-md-6'),
        ),
        'address_line',
        Row(
            Column(
                HTML(
                    '<a href="{{ view.success_url }}" class="btn btn-danger btn-sm mr-2">Cancelar</a>'
                    '<button type="submit" class="btn btn-primary btn-sm">Finalizar</button>'),
                css_class='pull-right'
            ),
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_csrf = True
        self.helper = FormHelper()
        self.helper.layout = self.layout

    class Meta:
        model = CustomerAddress
        fields = ['customer', 'street', 'number', 'city', 'state', 'cep', 'address_line']
