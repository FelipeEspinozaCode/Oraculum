import asyncio
import os
from oraculum import OracleDomain, InterpretationDepth
from services.oracle_service import OracleService

async def test_triple_redundancy():
    # Forzamos fallo de Nivel 1 eliminando la Key en el entorno de ejecución
    os.environ["DEEPSEEK_API_KEY"] = ""
    
    service = OracleService()
    
    print("\n--- LANZANDO CONSULTA (SIMULANDO FALLO DE IA) ---")
    # Probamos con Numerología y Astrología simultáneamente
    query = "Cual es mi destino hoy?"
    
    # 1. Prueba de Numerología
    res_num = await service.consult(OracleDomain.NUMEROLOGY, query, InterpretationDepth.BASIC)
    print(f"\n[DOMINIO: {res_num['domain'].upper()}]")
    print(f"NARRATIVA: {res_num['narrative']}")
    
    # 2. Prueba de Astrología
    res_astro = await service.consult(OracleDomain.ASTROLOGY, query, InterpretationDepth.BASIC)
    print(f"\n[DOMINIO: {res_astro['domain'].upper()}]")
    print(f"NARRATIVA: {res_astro['narrative']}")

if __name__ == "__main__":
    asyncio.run(test_triple_redundancy())
