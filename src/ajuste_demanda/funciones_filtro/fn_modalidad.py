"""
funciones_modalidad.py

Contiene funciones para manejar excepciones respecto a cambios de modalidad
"""
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.ajuste_demanda.funciones_filtro.utils.parseador_demanda import obtiene_parametro_consulta
from src.data_objects.demanda import Demanda


def correccion_asignaturas_online(demanda: Demanda, sesion: Session) -> bool:
    """
    Determina si la demanda analizada requiere corrección de modalidad a online
    según las excepciones manejadas internamente.
    """
    param = obtiene_parametro_consulta(demanda)

    query = text("SELECT \
                 pkg_consolidador_demanda.correccion_asignaturas_online(\
                 Demanda(:peri, :sede, :inst, :jorn, :plan, :nive, :moda, :asig, :dema)) \
                 FROM dual")

    evaluacion = sesion.execute(query, param).scalar()

    return evaluacion
