#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 18/07/2020 15:10.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from .models import *


class Config(LoginRequiredMixin, View):
    template = 'config/view.html'
    title = 'Configurações'
    subtitle = 'Configuração do sistema'

    def get(self, request):
        links = {
            'brand': {
                'name': "Marcas",
                'link': reverse_lazy('config-brand'),
                'quantity': Brand.objects.all().count(),
            },
            'model': {
                'name': "Modelos",
                'link': reverse_lazy('config-model'),
                'quantity': Model.objects.all().count(),
            },
            'type': {
                'name': "Tipos",
                'link': reverse_lazy('config-type'),
                'quantity': Type.objects.all().count(),
            },
            'capacity': {
                'name': "Capacidades",
                'link': reverse_lazy('config-capacity'),
                'quantity': Capacity.objects.all().count(),
            },
        }
        context = {
            'title': self.title,
            'subtitle': self.subtitle,
            'links': links
        }
        return render(request, self.template, context)
