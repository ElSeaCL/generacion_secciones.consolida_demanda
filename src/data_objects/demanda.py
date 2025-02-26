"""
demanda.py

Demanda
"""

from dataclasses import dataclass

@dataclass
class Demanda:
    """
    Contiene la demanda estimada a nivel de asignatura, plan y nivel.
    """

    plan: PlanEstudios
    nivel: int
    demanda: int