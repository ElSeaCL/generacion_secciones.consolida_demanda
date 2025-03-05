"""
main.py

"""
import timeit

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.ajuste_demanda.evaluador_demanda import EvaluadorDemandaAgrupada, EvaluadorDemandaIndividual
from src.ajuste_demanda.funciones_evalua.fn_cumple_demanda_minima import fn_incumple_demanda_minima
from src.ajuste_demanda.funciones_filtro.fn_planes_descontinuados import fn_planes_descontinuados
from src.ajuste_demanda.funciones_valores.fn_valor_cupo import fn_valor_fijo_cupo
from src.ajuste_demanda.obtenedor_valor import ObtenedorValorFijo
from src.consolidador_demanda import ConsolidadorDemanda
from src.DAL.repositorio_demanda import obtiene_demandas, obtiene_sedes
from src.ajuste_demanda.funciones_filtro.fn_modalidad import correccion_asignaturas_online
from src import configuration

# Parametros
peri_ccod = 240

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

# demanda total
demanda_total = sum(
    [sum(
        [demanda.demanda for demanda in demanda_sede[sede]]
    ) 
         for sede in demanda_sede.keys()]
)

def fn_asignaturas_online(demandas):
    fn_filtra_algo = lambda x: correccion_asignaturas_online(demanda=x, sesion=sesion)
    return list(filter(fn_filtra_algo, demandas))

evaluador_ejemplo1 = EvaluadorDemandaIndividual(fn_asignaturas_online)
fn_filtra = lambda x: fn_planes_descontinuados(demandas=x ,asig_ccod='FGDP01', institucion=1)
fn_evalua = lambda x: fn_incumple_demanda_minima(demandas=x, valor_minimo=12)
evaluador_ejemplo2 = EvaluadorDemandaAgrupada(fn_filtra, fn_evalua)

filtrado_1 = evaluador_ejemplo1.filtra(demanda_sede[2])
evaluado_1 = evaluador_ejemplo1.evalua(filtrado_1)

filtrado_2 = evaluador_ejemplo2.filtra(demanda_sede[2])
evaluado_2 = evaluador_ejemplo2.evalua(filtrado_2)

fn_valor = lambda: fn_valor_fijo_cupo(50)
#obtenedor_valor = ObtenedorValorFijo()



# probando la función
h1 = timeit.default_timer()
for ds in demanda_sede.values():
    for demanda in ds:
        resultado = correccion_asignaturas_online(demanda, sesion)
h2 = timeit.default_timer()

print('')
