#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 09/08/2020 11:09.
from crispy_forms.bootstrap import FieldWithButtons, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Row, Div, Field, Column
from django import forms
from django.forms import modelformset_factory

from .models import *


class OrderOfServiceForm(forms.ModelForm):
    prefix = "orderOfService"

    layout = Layout(
        Row(
            Field('type_of_service', wrapper_class='col-md-9'),
            Field('scheduled', wrapper_class='col-md-3 text-center mx-auto my-3'),
            Field('status', wrapper_class='col-md-12'),
            Field('start_date', wrapper_class='col-lg-6'),
            Field('end_date', wrapper_class='col-lg-6'),
            Field('defect', wrapper_class='col-md-12'),
            Field('observation', wrapper_class='col-md-12'),
            css_class='form-row',
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
            'defect': forms.Textarea(attrs={"rows": 4}),
            'observation': forms.Textarea(attrs={"rows": 4}),
        }
        fields = ['type_of_service', 'status', 'start_date', 'end_date',
                  'defect', 'observation', 'scheduled']


class PartsExchangedNewFormSetHelper(FormHelper):
    prefix = "partsFormSet"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_csrf = True
        self.form_tag = False
        self.layout = Layout(
            Row(
                Field('part', wrapper_class='col-md-12'),
                Field('quantity', wrapper_class='col-md-12'),
                HTML(
                    '<button class="btn btn-sm btn-danger remove-form-row">'
                    'remover'
                    '</button>'
                ),
                Field('id')
            ),
        )


class PartsExchangedEditFormSetHelper(FormHelper):
    prefix = "partsFormSet"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_csrf = True
        self.form_tag = False
        self.layout = Layout(
            Row(
                Field('part', wrapper_class='col-md-12'),
                Field('quantity', wrapper_class='col-md-12'),
                HTML(
                    '<button class="btn btn-sm btn-danger remove-form-row">'
                    'remover'
                    '</button>'
                ),
                Field('DELETE', wrapper_class='col-md-6'),
                Field('id'),
            ),
        )


PartsExchangedFormSet = modelformset_factory(
    PartsExchanged,
    fields='__all__',
    extra=1,
    can_delete=True
)
