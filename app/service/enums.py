#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 02/08/2020 11:21.
from enum import Enum


class ServiceStatusEnum(Enum):
    NOVO = 0
    EM_ANDAMENTO = 1
    FINALIZADO = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
