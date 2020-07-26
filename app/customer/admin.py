#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 25/07/2020 22:44.

from django.contrib import admin

from .models import *

admin.site.register(IndividualCustomer)
admin.site.register(JuridicalCustomer)
