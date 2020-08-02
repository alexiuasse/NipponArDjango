#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 02/08/2020 10:41.
from typing import Dict, Any

from customer.models import JuridicalCustomer, IndividualCustomer
from django.contrib.admin.utils import NestedObjects
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django_filters.views import FilterView
from django_tables2.paginators import LazyPaginator
from django_tables2.views import SingleTableMixin

from .conf import *
from .filters import *
from .forms import *
from .tables import *


class DeviceProfile(LoginRequiredMixin, View):
    template = 'device/profile.html'
    title = TITLE_VIEW_DEVICE
    subtitle = SUBTITLE_DEVICE

    def get(self, request, cpk, ctp, pk):
        header = HEADER_CLASS_DEVICE

        context = {
            'config': {
                'header': header
            },
            'obj': Device.objects.get(pk=pk),
            'cpk': cpk,
            'ctp': ctp,
        }
        return render(request, self.template, context)


class DeviceIndex(LoginRequiredMixin, View):
    template = 'device/view.html'
    title = TITLE_VIEW_DEVICE
    subtitle = SUBTITLE_DEVICE

    def get(self, request):
        links = {
            'Equipamentos': {
                'config': {
                    'header': HEADER_CLASS_DEVICE,
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
    title = TITLE_VIEW_DEVICE
    subtitle = SUBTITLE_DEVICE
    new = reverse_lazy('device:index')
    # new = reverse_lazy('device:create')
    header_class = HEADER_CLASS_DEVICE


class DeviceCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Device
    form_class = DeviceForm
    template_name = 'base/form.html'
    permission_required = 'device.create_device'
    title = TITLE_CREATE_DEVICE
    subtitle = SUBTITLE_DEVICE
    header_class = HEADER_CLASS_DEVICE

    def get_success_url(self):
        return reverse_lazy('customer:profile', kwargs={'pk': self.kwargs['cpk'], 'tp': self.kwargs['ctp']})

    def form_valid(self, form):
        response = super(DeviceCreate, self).form_valid(form)
        if self.object:
            customer = IndividualCustomer.objects.get(pk=self.kwargs['cpk']) if self.kwargs['ctp'] == 0 \
                else JuridicalCustomer.objects.get(pk=self.kwargs['cpk'])
            customer.devices.add(self.object)
        return response


class DeviceEdit(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Device
    form_class = DeviceForm
    template_name = 'base/form.html'
    permission_required = 'device.edit_device'
    title = TITLE_EDIT_DEVICE
    subtitle = SUBTITLE_DEVICE
    header_class = HEADER_CLASS_DEVICE

    def get_delete_url(self):
        return reverse_lazy('device:delete',
                            kwargs={'cpk': self.kwargs['cpk'], 'ctp': self.kwargs['ctp'], 'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        return super(DeviceEdit, self).get_context_data(**kwargs)


class DeviceDel(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Device
    template_name = "base/confirm_delete.html"
    permission_required = 'device.del_device'
    title = TITLE_DEL_DEVICE
    subtitle = SUBTITLE_DEVICE
    header_class = HEADER_CLASS_DEVICE

    def get_success_url(self):
        return reverse_lazy('customer:profile', kwargs={'pk': self.kwargs['cpk'], 'tp': self.kwargs['ctp']})

    def get_context_data(self, **kwargs):
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        collector = NestedObjects(using='default')  # or specific database
        collector.collect([context['object']])
        to_delete = collector.nested()
        context['extra_object'] = to_delete
        return context
