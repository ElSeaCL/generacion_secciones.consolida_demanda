"""
demanda.py

Contiene el data base object que permite recuperar datos de demanda
"""
from .base import Base, Column, String, Integer

class Demanda(Base):
    """
    Mapeao a la tabla gestion.opt_demanda_sede
    """
    __tablename__ = "opt_demanda_sede"

    peri_ccod = Column(Integer(), primary_key=True)
    sede_ccod = Column(Integer(), primary_key=True)
    inst_ccod = Column(Integer(), primary_key=True)
    jorn_ccod = Column(Integer(), primary_key=True)
    plan_ccod = Column(Integer(), primary_key=True)
    nive_ccod = Column(Integer(), primary_key=True)
    moda_ccod = Column(Integer(), primary_key=True)
    espe_ccod = Column(String(255))
    asig_ccod = Column(String(254), primary_key=True)
    area_ccod = Column(Integer())
    demanda  = Column(Integer())
