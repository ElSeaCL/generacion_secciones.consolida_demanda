"""
fabrica_evaluador.py

Contiene clases tipo ábrica utilizadas para manejar la creación de las instancias
de la clase AbsObtenedorValor
"""
from inspect import getmembers, isclass, isabstract, signature
from typing import Dict

import src.ajuste_demanda.evaluador_demanda as evaluar_demanda
from src.ajuste_demanda.funciones import registro_funciones


class EvaluadorFactory:

    evaluadores = {}

    def __init__(self):
        self._carga_evaluadores()

    def _carga_evaluadores(self):
        self.evaluadores = evaluar_demanda.AbsEvaluadorDemanda._registro

    def crea_instancia(self, configuracion: Dict) -> evaluar_demanda.AbsEvaluadorDemanda:
        clase = self.evaluadores[configuracion.pop('tipo')]

        # parametros requeridos
        params = signature(clase).parameters

        # obtengo las funciones
        params = {key: registro_funciones[parametro] 
                  for key, parametro in configuracion.items()}

        return clase(**params)
