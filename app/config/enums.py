#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 05/08/2020 17:03.
from enum import Enum


class StatusBadgeEnum(Enum):
    VERDE = "badge-success"
    AZUL = "badge-primary"
    CIANO = "badge-info"
    AMARELO = "badge-warning"
    VERMELHO = "badge-danger"
    CINZA = "badge-default"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
