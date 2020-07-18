#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 18/07/2020 14:13.

from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import *

admin.site.register(Brand, SimpleHistoryAdmin)
admin.site.register(Type, SimpleHistoryAdmin)
admin.site.register(Model, SimpleHistoryAdmin)
admin.site.register(Capacity, SimpleHistoryAdmin)
