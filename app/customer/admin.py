#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 10/07/2020 09:20.

from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Address)
