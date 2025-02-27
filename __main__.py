"""
main.py

"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.consolidador_demanda import ConsolidadorDemanda
from src.DAL.repositorio_demanda import obtiene_demandas, obtiene_sedes
from src import configuration

# Parametros
peri_ccod = 246

# base de datos
path = f"oracle+cx_oracle://{configuration.database['usuario']}:{configuration.database['password']}@{configuration.database['esquema']}" # pylint:disable=E1101
engine = create_engine(path)
session = sessionmaker(bind=engine)
sesion = session()

sedes = obtiene_sedes(peri_ccod, sesion)
demanda_sede = {}
for sede_ccod in sedes:
    demandas = obtiene_demandas(peri_ccod, sede_ccod, sesion)
    demanda_sede.update({sede_ccod:demandas})

print('En este punto debería tener disponible la configuración')
