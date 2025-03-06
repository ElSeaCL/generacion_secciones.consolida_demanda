"""
abs_obtenedor_valor.py


"""
import abc
from typing import Callable, Union

from src.data_objects.demanda import Demanda

class AbsObtenedorValor(abc.ABC):
    """
    Clase encargada de encontrar el valor a ajustar.
    """

    _funcion_valor: Callable = None

    @abc.abstractmethod
    def obtiene_valor(self, demanda: Demanda) -> Union[str, int]:
        """Retorna el valor a utilizar para modificar"""