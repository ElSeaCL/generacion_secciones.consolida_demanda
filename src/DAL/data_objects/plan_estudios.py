"""
plan_estudios.py

Contiene el data base object que permite recuperar datos del plan de estudios
"""
from .base import Base, Column, String, Date, Integer

class PlanEstudios(Base):
    """
    Mapeao a la tabla siga.plan_estudios
    """
    __tablename__ = "planes_estudioopt_demanda_sede"
    __table_args__ = {'schema' : 'siga'}

    plan_ccod = Column(Integer())
    espe_ccod = Column(String(4))
    plan_tdesc = Column(String(80))
    plan_ncorrelativo = Column(Integer())
