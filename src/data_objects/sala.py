"""
sala.py

Contiene datos de la sala.
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class Sala:
    """
    Data class de sala.
    """
    id: int
    nombre: str
    tipo_sala: int
    estado: int
    sede: int
    cupo: int
    