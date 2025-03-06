"""
fabrica_evaluador.py

Contiene clases tipo ábrica utilizadas para manejar la creación de las instancias
de la clase AbsObtenedorValor
"""
from inspect import getmembers, isclass, isabstract
from typing import Dict
import src.ajuste_demanda.evaluador_demanda as evaluar_demanda


class EvaluadorFactory:

    evaluadores = {}

    def __init__(self):
        self._carga_evaluadores()

    def _carga_evaluadores(self):
        clases = getmembers(evaluar_demanda, lambda x: isclass(x) and not isabstract(x))

        for nombre, _type in clases:
            if isclass(_type) and issubclass(_type, evaluar_demanda.AbsEvaluadorDemanda):
                self.evaluadores.update([[nombre, _type]])

    def crea_instancia(self, configuracion: Dict) -> evaluar_demanda.AbsEvaluadorDemanda:
        pass