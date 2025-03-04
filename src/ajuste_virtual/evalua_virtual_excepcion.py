"""

"""

from typing import Callable, List

from src.data_objects import Demanda
from src.ajuste_virtual.evaluador import EvaluadorDemandaVirtual


class EvaluadorDemandaAgrupadaExcepcion(EvaluadorDemandaVirtual):
    """
    
    """
    def __init__(
            self,
            funcion_agrupacion: Callable[[List[Demanda]],List[Demanda]],
            minimo_demanda: int) -> None:
        self._funcion = funcion_agrupacion
        self._minimo = minimo_demanda

    def evalua(self, demandas):

        # obtengo la suma de demandas
        total_demanda = sum([demanda.demanda for demanda in demandas])

        return total_demanda <= self._minimo

class EvaluadorDemandaIndividual(EvaluadorDemandaVirtual):
    """
    
    """
    def evalua(self, demandas):
        return True
