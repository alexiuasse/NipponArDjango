#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 17/07/2020 11:56.

from django.contrib import admin

from .models import *

admin.site.register(Brand)
admin.site.register(Type)
admin.site.register(Unit)
admin.site.register(Model)
admin.site.register(Capacity)
