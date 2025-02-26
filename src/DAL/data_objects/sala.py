"""
sala.py

Contiene el data base object que permite recuperar datos de salas
"""
from .base import Base, Column, String, Date, Integer

class Sala(Base):
    """
    Mapeao a la tabla siga.plan_estudios
    """
    __tablename__ = "planes_estudio"
    __table_args__ = {'schema' : 'siga'}

    sala_ccod = Column(Integer())
    tsal_ccod = Column(Integer())
    sede_ccod = Column(Integer())
    sala_tdesc = Column(String(100))
    sala_ciso = Column(String(50))
