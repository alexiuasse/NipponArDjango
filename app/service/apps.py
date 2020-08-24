#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/08/2020 18:25.

from django.apps import AppConfig


class ServiceConfig(AppConfig):
    name = 'service'

    def ready(self):
        import service.signals
