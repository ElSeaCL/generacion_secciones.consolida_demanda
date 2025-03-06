"""

"""
from typing import List

from src.data_objects.demanda import Demanda
from src.ajuste_demanda.funciones.utils import registro

@registro("planes descontinuados")
def fn_planes_descontinuados(demandas: List[Demanda], asig_ccod: str, institucion: int) -> List[Demanda]:
    inst = (1,2) if institucion in (1,2) else (8,)
    return [demanda for demanda in demandas if
            (demanda.asignatura.nombre == asig_ccod) and
            (demanda.plan.vigente == 2) and
            (demanda.institucion in inst)]
