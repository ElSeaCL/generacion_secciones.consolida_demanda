"""
repositorio_demanda.py

Funciones que permiten la obtención de los datos necesario para compilar la demanda

"""
#from .data_objects import *
from typing import Dict, List

from sqlalchemy.orm import Session


import src.DAL.data_objects as dbo
import src.data_objects as do

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
            asignatura = obtiene_asignatura(asig_ccod, peri_ccod)
            asignaturas.update({asig_ccod:asignatura})
        else:
            asignatura = asignaturas[asig_ccod]

        # buscamos la asignatura
        plan_ccod = demanda.plan_ccod
        if plan_ccod not in planes_estudio:
            plan = obtiene_planes(plan_ccod, peri_ccod)
            planes_estudio.update({plan_ccod:plan})
        else:
            plan = planes_estudio[plan_ccod]

        coleccion_demandas.append(
            do.Demanda(
                asignatura_original=asignatura,
                asignatura=asignatura,
                plan=plan,
                nivel=demanda.nive_ccod,
                demanda=demanda.demanda
            )
        )

    return coleccion_demandas

def obtiene_asignatura(asig_ccod: str, peri_ccod: int) -> do.Asignatura:
    
    asignatura: do.Asignatura = None
    return asignatura


def obtiene_planes(plan_ccod: int, peri_ccod: int) -> do.PlanEstudios:

    plan: do.PlanEstudios = None
    return plan


def obtiene_salas():
    pass
