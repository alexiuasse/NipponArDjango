#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 14/08/2020 19:56.
from datetime import datetime

from config.models import StatusService
from customer.models import IndividualCustomer, JuridicalCustomer
from django.urls import reverse
from service.models import OrderOfService

from frontend.icons import ICON_ADD, ICON_EYE, ICON_DASHBOARD, ICON_SERVICE


def context_dashboard():
    # current_week = datetime.today().isocalendar()[1]
    services = {
        'services_today': {
            'subheader': "Serviços Agendados para Hoje",
            'header': OrderOfService.objects.filter(scheduled=True, date=datetime.today()).count(),
            'bg': 'bg-triangle-top-primary',
            'chart_id': 'chart-services-today',
            'links': {
                'Ver': {
                    'link': reverse(
                        'service:index',
                        kwargs={
                            'status': 0,
                            'day': datetime.today().day,
                            'month': datetime.today().month,
                            'year': datetime.today().year,
                            'scheduled': 1
                        }),
                    'icon': ICON_EYE,
                    'contextual': 'primary',
                }
            },
        },
        'service': {
            'subheader': "Total de serviços em {}".format(datetime.today().year),
            'header': OrderOfService.objects.filter(date__year=datetime.today().year).count(),
            'chart_id': 'chart-services',
            'bg': 'bg-triangle-top-primary',
            'links': {
                'Ver': {
                    'link': reverse(
                        'service:index',
                        kwargs={
                            'status': 0,
                            'day': 0,
                            'month': 0,
                            'year': datetime.today().year,
                            'scheduled': 0
                        }),
                    'icon': ICON_EYE,
                    'contextual': 'primary',
                }
            },
        },
    }
    charts = {
        'chart-services': {
            'label': ["%d-%d-01" % (datetime.today().year, month) for month in range(1, 13)],
            'data': [
                OrderOfService.objects.filter(date__month=month, date__year=datetime.today().year).count()
                for month in range(1, 13)
            ],
            'series_name': 'Serviços',
            'type': "area",
            'color': '#206bc4',
        },
        'chart-individualcustomer': {
            'label': ["%d-%d-01" % (datetime.today().year, month) for month in range(1, 13)],
            'data': [
                IndividualCustomer.objects.filter(created_in__year=datetime.today().year,
                                                  created_in__month=month).count()
                for month in range(1, 13)
            ],
            'series_name': "Clientes",
            'type': "bar",
            'color': '#206bc4',
        },
        'chart-juridicalcustomer': {
            'label': ["%d-%d-01" % (datetime.today().year, month) for month in range(1, 13)],
            'data': [
                JuridicalCustomer.objects.filter(created_in__year=datetime.today().year,
                                                 created_in__month=month).count()
                for month in range(1, 13)
            ],
            'series_name': "Clientes",
            'type': "bar",
            'color': '#206bc4',
        },
    }
    for s in StatusService.objects.all():
        services[s.name] = {
            'subheader': "Status - {}".format(s.name),
            'header': OrderOfService.objects.filter(status=s, date__month=datetime.today().month).count(),
            'chart_id': 'chart-{}'.format(s.name),
            'bg': 'bg-triangle-top-{}'.format(s.contextual),
            'links': {
                'Ver': {
                    'link': reverse(
                        'service:index',
                        kwargs={
                            'status': s.pk,
                            'day': 0,
                            'month': 0,
                            'year': datetime.today().year,
                            'scheduled': 0
                        }),
                    'icon': ICON_EYE,
                    'contextual': 'primary',
                }
            },
        }
        charts['chart-{}'.format(s.name)] = {
            'label': ["%d-%d-01" % (datetime.today().year, month) for month in range(1, 13)],
            'data': [
                OrderOfService.objects.filter(status=s, date__month=month, date__year=datetime.today().year).count()
                for month in range(1, 13)
            ],
            'series_name': 'Serviços',
            'type': "area",
            'color': '#206bc4',
        }

    customers = {
        'Pessoa Física': {
            'subheader': "Captação de Clientes {}".format(datetime.today().year),
            'header': "Pessoa Física",
            'bg': 'bg-triangle-top-primary',
            'chart_id': 'chart-individualcustomer',
            'links': {
                'Novo': {
                    'link': reverse('customer:individualcustomer:create'),
                    'icon': ICON_ADD,
                    'contextual': 'success',
                },
                'Ver': {
                    'link': reverse('customer:individualcustomer:view'),
                    'icon': ICON_EYE,
                    'contextual': 'primary',
                }
            },
        },
        'Pessoa Jurídica': {
            'subheader': "Captação de Clientes {}".format(datetime.today().year),
            'header': "Pessoa Jurídica",
            'bg': 'bg-triangle-top-primary',
            'chart_id': 'chart-juridicalcustomer',
            'links': {
                'Novo': {
                    'link': reverse('customer:juridicalcustomer:create'),
                    'icon': ICON_ADD,
                    'contextual': 'success',
                },
                'Ver': {
                    'link': reverse('customer:juridicalcustomer:view'),
                    'icon': ICON_EYE,
                    'contextual': 'primary',
                }
            },
        }
    }

    page = {
        'Dashboard': {
            'pre_title': "Resumo",
            'title': {
                'text': "Dashboard",
                'icon': ICON_DASHBOARD,
            },
            'data': {
                'customers': customers,
            }
        },
        'Services': {
            'pre_title': "Resumo",
            'title': {
                'text': "Serviços",
                'icon': ICON_SERVICE,
            },
            'data': {
                'services': services,
            }
        }
    }

    return {
        'page': page,
        'charts': charts,
    }
