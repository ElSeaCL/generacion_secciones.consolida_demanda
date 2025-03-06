"""
fn_cumple_demanda_minima.py
"""

from typing import List

from src.data_objects.demanda import Demanda


def fn_incumple_demanda_minima(demandas: List[Demanda], valor_minimo: int) -> bool:
    return sum([demanda.demanda for demanda in demandas]) <= valor_minimo
