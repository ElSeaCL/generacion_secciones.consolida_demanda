"""
asignatura.py

Contiene el data base object que permite recuperar datos de asignaturas
"""
from .base import Base, Column, String, Integer

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
    Mapeao a la tabla siga.asignatura_periodos
    """
    __tablename__ = "asignatura_periodos"
    __table_args__ = {'schema' : 'siga'}

    asig_ccod = Column(String(6), primary_key=True)
    asig_nhoras_virtuales = Column(Integer())
    peri_ccod_inicio = Column(Integer(), primary_key=True)
    peri_ccod_termino = Column(Integer(), primary_key=True)
    asig_nhoras = Column(Integer())

class AsignaturaEquivalente(Base):
    """
    Mapeao a la tabla siga.asignaturas_equivalentes
    """
    __tablename__ = "asignaturas_equivalentes"
    __table_args__ = {'schema' : 'siga'}

    asig_ccod = Column(String(6), primary_key=True)
    asig_ccod_equiv = Column(String(6), primary_key=True)
    easieq_ccod = Column(Integer())

class AsignaturaExcepcion(Base):
    """
    Mapeo a la tabla opt_asignaturas_excepcion
    """
    __tablename__ = "opt_asignaturas_excepcion"

    peri_ccod = Column(Integer(), primary_key=True)
    asig_ccod = Column(Integer(), primary_key=True)
    oaon_tipo = Column(Integer(), primary_key=True)
    oaon_minimo = Column(Integer())
    oaon_maximo = Column(Integer())
    asig_ccod_equiv = Column(String(6))
    oaon_habilitado = Column(Integer())
    