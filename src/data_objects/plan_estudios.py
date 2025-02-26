"""
plan_estudios.py

Contiene datos del plan de estudios
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class PlanEstudios:
    """
    Data class del plan de estudios.
    """
    id: int
    nombre: str
    correlativo: int
    especialidad: str
    