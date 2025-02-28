"""
funciones_modalidad.py

Contiene funciones para manejar excepciones respecto a cambios de modalidad
"""
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.data_objects.demanda import Demanda


def correccion_asignaturas_online(demanda: Demanda, sesion: Session) -> bool:
    """
    Determina
    """
    periodo = demanda.periodo
    sede = demanda.sede
    institucion = demanda.institucion
    jornada = demanda.jornada
    plan = demanda.plan
    nivel = demanda.nivel
    modalidad = demanda.modalidad
    asignatura = demanda.asignatura_original.nombre
    cantidad_demanda = demanda.demanda

    query = text("SELECT \
                 pkg_consolidador_demanda.correccion_asignaturas_online(\
                 Demanda(:peri, :sede, :inst, :jorn, :plan, :nive, :moda, :asig, :dema)) \
                 FROM dual")
    param = {
        'peri':periodo,
        'sede':sede,
        'inst':institucion,
        'jorn':jornada,
        'plan':plan.id,
        'nive':nivel,
        'moda':modalidad,
        'asig':asignatura,
        'dema':cantidad_demanda}
    
    evaluacion = sesion.execute(query, param).scalar()

    return evaluacion