#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 18/07/2020 12:09.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from .models import *


class Config(LoginRequiredMixin, View):
    template = 'config/view.html'
    title = 'Configurações'
    subtitle = 'Configuração do sistema'

    def get(self, request):
        context = {
            'title': self.title,
            'subtitle': self.subtitle,
            'brand': Brand.objects.all().count(),
            'model': Model.objects.all().count(),
            'type': Type.objects.all().count(),
        }
        return render(request, self.template, context)
