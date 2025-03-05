"""
fn_valor_fijo.py

Retorna un valor fijo configurable. 
"""

from typing import Dict, List

from src.data_objects.sala import Sala


def fn_valor_fijo_cupo(cupo: int) -> int:
    return cupo

def fn_maximo_cupo_sede(salas: List[Sala]) -> int:
    return min(50, max([sala.cupo for sala in salas if
                (sala.tipo_sala == 1) and
                (sala.estado == 1)]
        )
    )

def fn_cupo_excepcion(valores_excepcion: Dict[str,int], asignatura: str) -> int:
    return valores_excepcion[asignatura]
