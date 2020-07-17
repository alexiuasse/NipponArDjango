#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 17/07/2020 11:56.

# users/models.py
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass
    # add additional fields in here
