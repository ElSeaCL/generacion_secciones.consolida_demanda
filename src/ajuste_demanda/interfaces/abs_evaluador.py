"""
abs_evaluador.py


"""
import abc
from typing import Callable, List

from src.data_objects.demanda import Demanda


class AbsEvaluadorDemanda(abc.ABC):
    """Evalua la demanda y determina si cumple con la excepción"""

    _funcion_filtro: Callable = None

    @abc.abstractmethod
    def filtra(self, demandas: List[Demanda]) -> List[Demanda]:
        """A partir de un listado de demandas filtra los valores 
        según los resultados de la función filtro"""

    @abc.abstractmethod
    def evalua(self, demandas: List[Demanda]) -> bool:
        """Evalua un listado de demandas y determina si requieren 
        un ajuste a sus valores."""