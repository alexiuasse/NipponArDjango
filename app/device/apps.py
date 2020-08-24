#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 24/08/2020 17:07.

from django.apps import AppConfig


class DeviceConfig(AppConfig):
    name = 'device'

    def ready(self):
        import device.signals
