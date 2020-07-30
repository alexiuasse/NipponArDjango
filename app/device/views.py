#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 30/07/2020 17:21.
from typing import Dict, Any

from django.conf import settings
from django.contrib.admin.utils import NestedObjects
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django_filters.views import FilterView
from django_tables2.paginators import LazyPaginator
from django_tables2.views import SingleTableMixin

from .filters import *
from .forms import *
from .tables import *
from .models import *


class DeviceIndex(LoginRequiredMixin, View):
    template = 'device/view.html'
    title = settings.TITLE_VIEW_DEVICE
    subtitle = settings.SUBTITLE_DEVICE

    def get(self, request):
        links = {
            'Equipamentos': {
                'config': {
                    'header': settings.HEADER_CLASS_DEVICE,
                },
                'Equipamentos': {
                    'name': "Equipamentos",
                    'link': reverse_lazy('device:view'),
                    'badge_text': Device.objects.count(),
                    'badge_class': 'badge-success',
                    'icon': 'person',
                },

            },
        }
        context = {
            'title': self.title,
            'subtitle': self.subtitle,
            'links': links
        }
        return render(request, self.template, context)


########################################################################################################################
class DeviceView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    model = Device
    table_class = DeviceTable
    filterset_class = DeviceFilter
    paginator_class = LazyPaginator
    permission_required = 'device.view_device'
    template_name = 'base/view.html'
    title = settings.TITLE_VIEW_DEVICE
    subtitle = settings.SUBTITLE_DEVICE
    new = reverse_lazy('device:create')
    header_class = settings.HEADER_CLASS_DEVICE


class DeviceCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Device
    form_class = DeviceForm
    template_name = 'base/form.html'
    permission_required = 'device.create_device'
    success_url = reverse_lazy('device:view')
    title = settings.TITLE_CREATE_DEVICE
    subtitle = settings.SUBTITLE_DEVICE
    header_class = settings.HEADER_CLASS_DEVICE


class DeviceEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Device
    form_class = DeviceForm
    template_name = 'base/form.html'
    permission_required = 'device.edit_device'
    success_url = reverse_lazy('device:view')
    title = settings.TITLE_EDIT_DEVICE
    subtitle = settings.SUBTITLE_DEVICE
    header_class = settings.HEADER_CLASS_DEVICE


class DeviceDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Device
    template_name = "base/confirm_delete.html"
    permission_required = 'device.del_device'
    success_url = reverse_lazy('device:view')
    title = settings.TITLE_DEL_DEVICE
    subtitle = settings.SUBTITLE_DEVICE
    header_class = settings.HEADER_CLASS_DEVICE

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context
