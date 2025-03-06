from .funciones_evalua import *
from .funciones_filtro import *
from .funciones_valores import *

registro_funciones = {obj.__nombre_personalizado__:obj
            for nombre, obj in locals().items()
            if callable(obj) and obj.__name__[:2] == 'fn'}