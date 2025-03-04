"""

"""

from typing import Dict, List, Callable

from src.data_objects.demanda import Demanda


class AjustadorDemandaVirtual:
    """
    Aplica las funciones necesarias para obtener la demanda que pertenece a sede
    virtual y la ajusta
    """

    def __init__(self, funciones_agregacion: List[Callable], funciones_unidad: List[Callable], ) -> None:
        pass

    def ajusta_demanda(self, demanda_sedes: Dict[int, Demanda]) -> None:
        """
        Toma las demandas por sede, separa las que pertenecen a sede virtual
        y las asociada a la sede que corresponde.
        """
        # Itera por cada sede
        for sede, demanda in demanda_sedes.items():

            # 1. aplicamos las funciones que revisan la demanda como grupo

            # 2. aplicamos las funciones que revisan la demanda individual

