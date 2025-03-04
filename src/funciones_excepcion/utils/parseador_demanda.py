"""

"""
from typing import Dict

from src.data_objects.demanda import Demanda

def obtiene_parametro_consulta(demanda: Demanda) -> Dict[str,int]:

    periodo = demanda.periodo
    sede = demanda.sede
    institucion = demanda.institucion
    jornada = demanda.jornada
    plan = demanda.plan
    nivel = demanda.nivel
    modalidad = demanda.modalidad
    asignatura = demanda.asignatura_original.nombre
    cantidad_demanda = demanda.demanda

    param = {
        'peri':periodo,
        'sede':sede,
        'inst':institucion,
        'jorn':jornada,
        'plan':plan.id,
        'nive':nivel,
        'moda':modalidad,
        'asig':asignatura,
        'dema':cantidad_demanda}

    return param