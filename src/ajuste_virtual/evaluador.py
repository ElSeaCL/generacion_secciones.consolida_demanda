"""

"""

from abc import ABC, abstractmethod
from typing import Callable, List

from src.data_objects.demanda import Demanda


class EvaluadorDemandaVirtual(ABC):

    def filtra(self, demandas: List[Demanda], funcion_filtro: Callable[[List[Demanda]], List[Demanda]]) -> List[Demanda]:
        return funcion_filtro(demandas)

    @abstractmethod
    def evalua(self, demandas: List[Demanda]) -> bool:
        pass