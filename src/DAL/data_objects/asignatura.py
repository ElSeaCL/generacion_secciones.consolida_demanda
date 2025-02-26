"""
asignatura.py

Contiene el data base object que permite recuperar datos de asignaturas
"""
from .base import Base, Column, String, Date, Integer

class Asignatura(Base):
    """
    Mapeao a la tabla siga.plan_estudios
    """
    __tablename__ = "asignaturas"
    __table_args__ = {'schema' : 'siga'}

    asig_ccod = Column(String(6), primary_key=True)
    tasg_ccod = Column(Integer())
    asig_tdesc = Column(String(200))
    asig_nhoras = Column(Integer())
    asig_nhoras_virtuales = Column(Integer)

class AsignaturaPeriodo(Base):
    """
    Mapeao a la tabla siga.plan_estudios
    """
    __tablename__ = "asignatura_periodos"
    __table_args__ = {'schema' : 'siga'}

    asig_ccod = Column(String(6), primary_key=True)
    asig_nhoras_virtuales = Column(Integer())
    peri_ccod_inicio = Column(Integer(), primary_key=True)
    peri_ccod_termino = Column(Integer(), primary_key=True)
    asig_nhoras = Column(Integer())
