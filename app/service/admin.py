#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 08/08/2020 11:24.

from django.contrib import admin

from .models import *

admin.site.register(OrderOfService)
admin.site.register(PartsExchanged)
