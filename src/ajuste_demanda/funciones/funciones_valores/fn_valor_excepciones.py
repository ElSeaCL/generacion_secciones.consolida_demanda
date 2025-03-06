"""
fn_valores_excepciones.py

función que permite retornar los valores de excepción.
"""

from typing import Dict, Union

from src.ajuste_demanda.funciones.utils import registro

@registro("valor excepcion")
def fn_valores_excepcion(excepciones: Dict[str,Union[int,str]], asignatura: str):
    # Con estos valores retorno un función que solo requiere de asignatura
    return excepciones[asignatura]
