"""
fabrica_obtenedor.py

Contiene clases tipo ábrica utilizadas para manejar la creación de las instancias
de la clase AbsObtenedorValor
"""
from inspect import getmembers, isclass, isabstract
import src.ajuste_demanda.obtenedor_valor as obtenedor_valor


class ObtenedorFactory:

    evaluadores = {}

    def __init__(self):
        self._carga_evaluadores()

    def _carga_evaluadores(self):
        clases = getmembers(obtenedor_valor, lambda x: isclass(x) and not isabstract(x))

        for nombre, _type in clases:
            if isclass(_type) and issubclass(_type, obtenedor_valor.AbsObtenedorValor):
                self.evaluadores.update([[nombre, _type]])