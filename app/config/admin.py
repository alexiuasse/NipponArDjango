#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 12/07/2020 20:01.

from django.contrib import admin
from .models import *

admin.site.register(Brand)
admin.site.register(Type)
admin.site.register(Unit)
admin.site.register(Model)
admin.site.register(Capacity)
