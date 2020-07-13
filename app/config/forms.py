from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Column, Div, HTML
from .models import *

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
        self.helper = FormHelper()
        self.helper.layout = self.layout

class BrandForm(BaseConfigForm):

    class Meta:
        model = Brand
        fields = '__all__'

class ModelForm(BaseConfigForm):

    class Meta:
        model = Model
        fields = '__all__'

class TypeForm(BaseConfigForm):

    class Meta:
        model = Type
        fields = '__all__'

class UnitForm(BaseConfigForm):

    class Meta:
        model = Unit
        fields = '__all__'

class CapacityForm(BaseConfigForm):
    layout = Layout(
        Div(
            Column('name', css_class='form-group col-md-3 mb-0 font-weight-bold'),
            Column('unit', css_class='form-group col-md-3 mb-0 font-weight-bold'),
        ),
        Div(
            Column(
                HTML(
                    '<a href="{{ redirect_success }}" class="btn btn-danger mr-2">Cancelar</a>'
                    '<button type="submit" class="btn btn-primary">Finalizar</button>'),
                    css_class='mb-3 mb-sm-0'
                ),
            css_class='row'
        ),
    )

    class Meta:
        model = Capacity
        fields = '__all__'
