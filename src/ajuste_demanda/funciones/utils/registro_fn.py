"""
registro_fn.py

Función de apoyo, permite registrar un nombre personalizado para cada función.
"""

def registro(nombre):
    def decorador(fn):
        fn.__nombre_personalizado__ = nombre
        return fn
    return decorador