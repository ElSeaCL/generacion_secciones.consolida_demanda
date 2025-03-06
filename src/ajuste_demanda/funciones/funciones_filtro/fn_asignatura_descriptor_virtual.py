"""

"""
from typing import List

from src.data_objects.demanda import Demanda
from src.ajuste_demanda.funciones.utils import registro

@registro("asignatura horas totales virtuales")
def fn_asignatura_virtual(demandas: List[Demanda]) -> List[Demanda]:
    return [demanda for demanda in demandas if
            demanda.asignatura.horas_semanales == \
                demanda.asignatura.horas_virtuales]
