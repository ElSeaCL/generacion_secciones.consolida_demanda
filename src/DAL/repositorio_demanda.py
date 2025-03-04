"""
repositorio_demanda.py

Funciones que permiten la obtención de los datos necesario para compilar la demanda

"""
#from .data_objects import *
from typing import Dict, List

from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound


import src.DAL.data_objects as dbo
import src.data_objects as do

def obtiene_sedes(peri_ccod: int, sesion: Session) -> List[int]:
    """
    Retorna listado de sedes
    """
    resultados = sesion.query(
        dbo.Demanda.sede_ccod).filter(
            dbo.Demanda.peri_ccod == peri_ccod).distinct(
                dbo.Demanda.sede_ccod).all()
    resultados = tuple([sede[0] for sede in resultados])

    return resultados

def obtiene_demandas(peri_ccod: int, sede_ccod: int, sesion: Session) -> List[do.Demanda]:
    """
    Retorna un listado de demandas
    """
    # asignaturas recolectada
    asignaturas: Dict[int,do.Asignatura] = {}
    # planes recolectados
    planes_estudio: Dict[int,do.PlanEstudios] = {}

    # Listado de retorno
    coleccion_demandas: List[do.Demanda] = []

    # Partimos determinando el universo de asignaturas
    codigos_asignaturas = sesion.query(
        dbo.Demanda.asig_ccod).filter(
            dbo.Demanda.peri_ccod == peri_ccod,
            dbo.Demanda.sede_ccod == sede_ccod
        ).distinct(dbo.Demanda.asig_ccod).all()
    codigos_asignaturas = [asig[0] for asig in codigos_asignaturas]

    # Realizamos la consulta
    resultados = sesion.query(dbo.Demanda).filter(
        dbo.Demanda.peri_ccod == peri_ccod,
        dbo.Demanda.sede_ccod == sede_ccod
        ).all()

    # iteramos en los resultados creando la demanda esperada
    for demanda in resultados:

        # buscamos la asignatura
        asig_ccod = demanda.asig_ccod
        if asig_ccod not in asignaturas:
            asignatura = obtiene_asignatura(asig_ccod, peri_ccod, codigos_asignaturas, sesion)
            asignaturas.update({asig_ccod:asignatura})
        else:
            asignatura = asignaturas[asig_ccod]

        # buscamos la asignatura
        plan_ccod = demanda.plan_ccod
        if plan_ccod not in planes_estudio:
            plan = obtiene_planes(plan_ccod, sesion)
            planes_estudio.update({plan_ccod:plan})
        else:
            plan = planes_estudio[plan_ccod]

        coleccion_demandas.append(
            do.Demanda(
                periodo=peri_ccod,
                sede=sede_ccod,
                institucion=demanda.inst_ccod,
                jornada=demanda.jorn_ccod,
                modalidad=demanda.moda_ccod,
                asignatura_original=asignatura,
                asignatura=asignatura,
                plan=plan,
                nivel=demanda.nive_ccod,
                demanda=demanda.demanda
            )
        )

    return coleccion_demandas

def obtiene_asignatura(
        asig_ccod: str,
        peri_ccod: int,
        asignaturas: List[str],
        sesion: Session) -> do.Asignatura:

    asignatura: do.Asignatura = None

    resultados_principal = sesion.query(
        dbo.Asignatura).filter(dbo.Asignatura.asig_ccod == asig_ccod).one()

    try:
        resultado_periodo = sesion.query(
            dbo.AsignaturaPeriodo).filter(
                dbo.AsignaturaPeriodo.asig_ccod == asig_ccod,
                dbo.AsignaturaPeriodo.peri_ccod_inicio <= peri_ccod,
                dbo.AsignaturaPeriodo.peri_ccod_termino > peri_ccod).one()
        asig_nhoras = resultado_periodo.asig_nhoras
        asig_nhoras_virtual = resultado_periodo.asig_nhoras_virtuales
    except NoResultFound:
        asig_nhoras = resultados_principal.asig_nhoras
        asig_nhoras_virtual = resultados_principal.asig_nhoras_virtuales

    resultado_equivalencias = sesion.query(
        dbo.AsignaturaEquivalente.asig_ccod_equiv).filter(
            dbo.AsignaturaEquivalente.easieq_ccod == 1,
            dbo.AsignaturaEquivalente.asig_ccod == asig_ccod,
            dbo.AsignaturaEquivalente.asig_ccod_equiv.in_(asignaturas)
            ).all()
    resultado_equivalencias = tuple([asig[0] for asig in resultado_equivalencias])

    asignatura = do.Asignatura(
        resultados_principal.asig_ccod,
        resultados_principal.tasg_ccod,
        asig_nhoras,
        0 if asig_nhoras_virtual is None else asig_nhoras_virtual,
        resultado_equivalencias
    )

    return asignatura

def obtiene_planes(plan_ccod: int, sesion: Session) -> do.PlanEstudios:

    plan: do.PlanEstudios = None

    resultado = sesion.query(dbo.PlanEstudios).filter(dbo.PlanEstudios.plan_ccod == plan_ccod).one()

    plan = do.PlanEstudios(
        resultado.plan_ccod,
        resultado.plan_tdesc,
        resultado.plan_ncorrelativo,
        resultado.espe_ccod,
        resultado.epes_ccod
    )

    return plan


def obtiene_salas():
    pass
