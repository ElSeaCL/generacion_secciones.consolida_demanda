"""
fitro_demanda.py
"""

from typing import Callable, List
from sqlalchemy.orm import Session
from src.data_objects.demanda import Demanda


def filtro_demanda(funcion: Callable, demandas: List[Demanda], sesion: Session):
    return filter(lambda x: funcion(demanda=x, sesion=sesion), demandas)
