"""
ajustador.py

Encargado de realizar el ajuste en los valores de demanda según lo definido.
"""

from typing import Union

from src.ajuste_demanda.interfaces.abs_evaluador import AbsEvaluadorDemanda
from src.ajuste_demanda.interfaces.abs_obtenedor_valor import AbsObtenedorValor
from src.data_objects.demanda import Demanda


class AjustadorDemanda:
    """Clase contiene el proceso completo requerido para ajustar los
    atributos de la demanda según los casos evaluados a partir de los 
    elementos."""

    def __init__(
            self,
            evaluador: AbsEvaluadorDemanda,
            obtenedor: AbsObtenedorValor,
            atributo: str):
        self._evaluador = evaluador
        self._obtenedor = obtenedor
        self._atributo = atributo

    def _actualiza_atributo(self, demanda: Demanda, valor: Union[str,int], atributo: str):

        # Determino si el atributo existe. En caso de que no sea así retorno excepción
        if hasattr(demanda, atributo):
            # En caso de que así: 
            # 1. almaceno el estado original
            # TODO parte pendiente

            # 2. actualizo con el valor proporcionado
            setattr(demanda, atributo, valor)

        else:
            raise AttributeError('Atributo no existente')
