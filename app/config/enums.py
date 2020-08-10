#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 10/08/2020 10:14.
from enum import Enum


class ContextualEnum(Enum):
    VERDE = "success"
    AZUL = "primary"
    CIANO = "info"
    AMARELO = "warning"
    VERMELHO = "danger"
    CINZA = "default"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
