"""

"""
from typing import List

from src.data_objects.demanda import Demanda


def fn_asignatura_virtual(demandas: List[Demanda]) -> List[Demanda]:
    return [demanda for demanda in demandas if
            demanda.asignatura.horas_semanales == \
                demanda.asignatura.horas_virtuales]
