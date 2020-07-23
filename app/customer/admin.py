#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 22/07/2020 17:27.

from django.contrib import admin

from .models import *

admin.site.register(Customer)
admin.site.register(CustomerAddress)
