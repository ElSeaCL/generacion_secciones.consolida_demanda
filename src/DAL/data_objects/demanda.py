"""
demanda.py

Contiene el data base object que permite recuperar datos de demanda
"""
from .base import Base, Column, String, Date, Integer

class Demanda(Base):
    """
    Mapeao a la tabla gestion.opt_demanda_sede
    """
    __tablename__ = "opt_demanda_sede"

    peri_ccod = Column(Integer())
    sede_ccod = Column(Integer())
    inst_ccod = Column(Integer())
    jorn_ccod = Column(Integer())
    plan_ccod = Column(Integer())
    nive_ccod = Column(Integer())
    moda_ccod = Column(Integer())
    espe_ccod = Column(String(255))
    asig_ccod = Column(String(254))
    area_ccod = Column(Integer())
    demanda  = Column(Integer())
