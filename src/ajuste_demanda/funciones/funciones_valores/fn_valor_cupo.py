"""
fn_valor_fijo.py

Retorna un valor fijo configurable. 
"""

from typing import Dict, List

from src.data_objects.sala import Sala
from src.ajuste_demanda.funciones.utils import registro

@registro("valor fijo")
def fn_valor_fijo_cupo(cupo: int) -> int:
    return cupo

@registro("máximo cupo sede")
def fn_maximo_cupo_sede(salas: List[Sala]) -> int:
    return min(50, max([sala.cupo for sala in salas if
                (sala.tipo_sala == 1) and
                (sala.estado == 1)]
        )
    )

@registro("cupo excepcion")
def fn_cupo_excepcion(valores_excepcion: Dict[str,int], asignatura: str) -> int:
    return valores_excepcion[asignatura]
