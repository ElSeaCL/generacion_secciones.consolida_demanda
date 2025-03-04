"""

"""
from typing import List

from src.data_objects.demanda import Demanda


def fn_planes_descontinuados(demandas: List[Demanda], asig_ccod: str) -> List[Demanda]:
    return [demanda for demanda in demandas if
            (demanda.asignatura.nombre == asig_ccod)]
