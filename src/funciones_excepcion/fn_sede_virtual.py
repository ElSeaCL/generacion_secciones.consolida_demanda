"""
funciones traspaso virtual


TODO: MODIFICAR

"""

from typing import List

from src.data_objects import Demanda


def obtiene_demanda_virtual_planes_descontinuados(demandas: List[Demanda], asignatura_excepcion: AsignaturaExcepcion) -> None:
    """
    Toma las demandas totales, determina si dentro estas existe un
    grupo que cumpla con el requerimiento de traspaso y en caso de que 
    así sea traspasa a sede virtual
    """
    
    demandas_filtradas = [demanda for demanda in demandas if demanda.plan.vigente == 2]
    #demandas_filtradas = [demanda for demanda in demandas_filtradas if ]

    cantidad_total = sum([demanda.demanda for demanda in demandas_filtradas])

    return demandas_filtradas

def obtiene_demanda_virtual_empleabilidad(demandas: List[Demanda]) -> None:
    """
    Toma las demandas totales, determina si dentro estas existe un
    grupo que cumpla con el requerimiento de traspaso y en caso de que 
    así sea traspasa a sede virtual
    """
    pass

def obtiene_demanda_virtual_descriptor_virtual(demandas: List[Demanda]) -> None:
    """
    Toma las demandas totales, determina si dentro estas existe un
    grupo que cumpla con el requerimiento de traspaso y en caso de que 
    así sea traspasa a sede virtual
    """
    pass
