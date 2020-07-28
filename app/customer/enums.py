#  Created by Alex Matos Iuasse.
#  Copyright (c) 2020.  All rights reserved.
#  Last modified 25/07/2020 23:18.
from enum import Enum


class TypeCustomerEnum(Enum):
    FISICA = "PF"
    JURIDICA = "PJ"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class StateEnum(Enum):
    ACRE = "AC"
    ALAGOAS = "AL"
    AMAPA = "AP"
    AMAZONAS = "AM"
    BAHIA = "BA"
    CEARA = "CE"
    DISTRITO_FEDERAL = "DF"
    ESPIRITO_SANTO = "ES"
    GOIAS = "GO"
    MARANHAO = "MA"
    MATO_GROSSO = "MT"
    MATO_GROSSO_DO_SUL = "MS"
    MINAS_GERAIS = "MG"
    PARA = "PA"
    PARAIBA = "PB"
    PARANA = "PR"
    PERNAMBUCO = "PE"
    PIAUI = "PI"
    RIO_DE_JANEIRO = "RJ"
    RIO_GRANDE_DO_NORTE = "RN"
    RIO_GRANDE_DO_SUL = "RS"
    RONDONIA = "RO"
    RORAIMA = "RR"
    SANTA_CATARINA = "SC"
    SAO_PAULO = "SP"
    SERGIPE = "SE"
    TOCANTINS = "TO"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
