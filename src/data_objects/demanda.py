"""
demanda.py

Demanda
"""

from dataclasses import dataclass

from .plan_estudios import PlanEstudios
from .asignatura import Asignatura

@dataclass
class Demanda:
    """
    Contiene la demanda estimada a nivel de asignatura, plan y nivel.
    """

    periodo: int
    sede: int
    institucion: int
    jornada: int
    modalidad: int
    asignatura_original: Asignatura
    asignatura: Asignatura
    plan: PlanEstudios
    nivel: int
    demanda: int
