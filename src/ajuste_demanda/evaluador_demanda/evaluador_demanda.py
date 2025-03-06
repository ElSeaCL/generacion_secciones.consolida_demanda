"""
Clases encargadas de evaluar en qué casos la demanda requiere
de un ajuste de su estado.
"""

from typing import Callable, List
from src.ajuste_demanda.evaluador_demanda.interfaces.abs_evaluador import AbsEvaluadorDemanda
from src.data_objects.demanda import Demanda


class EvaluadorDemandaIndividual(AbsEvaluadorDemanda):
    """
    Realiza una evaluación considerando cada demanda como una valor individual"""

    def __init__(self, funcion_filtro: Callable[[List[Demanda]], List[Demanda]]) -> List[Demanda]:
        self._funcion_filtro = funcion_filtro

    def filtra(self, demandas):
        return self._funcion_filtro(demandas)

    def evalua(self, demandas):
        return True

class EvaluadorDemandaAgrupada(AbsEvaluadorDemanda):
    """
    Realiza una evaluación considerando cada demanda como una valor individual"""

    def __init__(
            self,
            funcion_filtro: Callable[[List[Demanda]], List[Demanda]],
            funcion_evalua: Callable[[List[Demanda]], bool]
            ) -> List[Demanda]:
        self._funcion_filtro = funcion_filtro
        self._funcion_evalua = funcion_evalua

    def filtra(self, demandas):
        return self._funcion_filtro(demandas)

    def evalua(self, demandas):
        return self._funcion_evalua(demandas)