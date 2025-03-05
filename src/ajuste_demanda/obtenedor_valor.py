"""
obtenedor_valor.py

Clases utilizadas para obtener los valores a modificar.
"""

from typing import Callable

from src.ajuste_demanda.interfaces.abs_obtenedor_valor import AbsObtenedorValor


class ObtenedorValorFijo(AbsObtenedorValor):
    """Obtiene un valor como un número fijo"""

    def __init__(self, funcion_valor: Callable):
        self._funcion_valor = funcion_valor

    def obtiene_valor(self, demanda):
        return self._funcion_valor()

class ObtenedorValorExcepcionAsignatura(AbsObtenedorValor):
    """Obtiene un valor a partir de los definido en las excepciones por
    asignatura.
    
    La función valor que funciona como parte del constructor se encarga
    de retornar el valor requerido"""

    def __init__(self, funcion_valor: Callable):
        self._funcion_valor = funcion_valor

    def obtiene_valor(self, demanda):
        asignatura = demanda.asignatura.nombre
        return self._funcion_valor(asignatura)
        


    