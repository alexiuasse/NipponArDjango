#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 10/08/2020 12:51.

from django.conf import settings  # import the settings file


def enterprise_name(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'NAME_OF_ENTERPRISE': settings.NAME_OF_ENTERPRISE, 'VERSION': settings.VERSION}
