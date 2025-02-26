"""
asignatura.py

Contiene datos de la asignatura.
"""

from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Asignatura:
    """
    Data class de asignatura
    """
    nombre: str
    horas_semanales: int
    horas_virtuales: int

    _asignaturas_equivalentes: List['Asignatura']

    def __eq__(self, asignatura: 'Asignatura'):
        return asignatura.nombre in self._asignaturas_equivalentes

@dataclass(frozen=True)
class InstanciaAsignatura:
    """
    Asignatura vista a nivel de periodo, sede, institución, jornada y 
    modalidad
    """
    asignatura: Asignatura
    periodo: int
    sede: int
    institucion: int
    jornada: int
    modalidad: int
