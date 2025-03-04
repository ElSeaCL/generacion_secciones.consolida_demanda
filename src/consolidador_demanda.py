"""
Consolidador de Demanda

Archivo que contiene el flujo principal del consolidador de demanda
"""

from typing import Dict, Tuple

from src.data_objects.demanda import Demanda


class ConsolidadorDemanda:
    """
    Contiene el flujo mediante el cual se realiza la agrupación de las 
    demandas compactables, el cual sirve como input para la generación
    de secciones.
    """

    def __init__(self, demandas_sede: Dict[int,Demanda]) -> None:
        self._demandas_sede = demandas_sede

    def inicio(self) -> Tuple[Demanda]:
        """
        Inicia el proceso de generación de los grupos compactables
        de demanda.
        """


        # Itera por sede
        for sede_ccod, demandas in self._demandas_sede.items():

            ajustador_demanda_virtual(demanda)

            for demanda in demandas:
                pass
            

            #Itero por demanda
            

        # Aplica las excepciones para cambio de sede
        # caso aplicable para la generación de demanda virtual

        # Generación de salas por asignatura

        # Obtención de cupo por demanda

        # Aplicación de excepciones de cupo de sala

        # Aplicación de excepciones varias
