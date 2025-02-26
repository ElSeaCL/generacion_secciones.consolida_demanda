"""
base.py

Contiene elementos comunes para la conexión a la base de datos
"""

from sqlalchemy import Column, Date, DateTime, Integer, Sequence, String, MetaData, DATE
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = MetaData()

