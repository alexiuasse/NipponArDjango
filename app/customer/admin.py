#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 17/07/2020 11:56.

from django.contrib import admin

from .models import *

admin.site.register(Customer)
admin.site.register(Address)
