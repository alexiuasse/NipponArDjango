#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 19/08/2020 10:09.
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Row, Field
from django import forms
from django.forms import modelformset_factory

from .models import *


class OrderOfServiceForm(forms.ModelForm):
    prefix = "orderOfService"

    layout = Layout(
        Row(
            Field('type_of_service', wrapper_class='col-md'),
            Field('status', wrapper_class='col-md'),
            Field('date', wrapper_class='col-md'),
            Field('defect', wrapper_class='col-md'),
            Field('observation', wrapper_class='col-md'),
            Field('scheduled', wrapper_class='col-md mt-3'),
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
            'date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'defect': forms.Textarea(attrs={"rows": 4}),
            'observation': forms.Textarea(attrs={"rows": 4}),
        }
        fields = ['type_of_service', 'status', 'date',
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
                    '<button class="btn btn-sm btn-danger remove-form-row mt-2 mb-1">'
                    'remover'
                    '</button>'
                ),
                Field('id'),
                css_class="form-clone-row"
            )
        )


class PartsExchangedEditFormSetHelper(FormHelper):
    prefix = "partsFormSet"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_csrf = True
        self.form_tag = False
        self.layout = Layout(
            Row(
                Field('part', wrapper_class='col-md'),
                Field('quantity', wrapper_class='col-md'),
                HTML(
                    '<button class="btn btn-sm btn-danger remove-form-row mt-2 mb-1">'
                    'Remover'
                    '</button>'
                ),
                Field('DELETE', wrapper_class='col-md'),
                Field('id'),
                css_class="form-clone-row"
            )
        )


PartsExchangedFormSet = modelformset_factory(
    PartsExchanged,
    fields='__all__',
    extra=1,
    can_delete=True
)
