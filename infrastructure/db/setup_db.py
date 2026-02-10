from infrastructure.db.database import engine, Base
from infrastructure.db.session import SessionLocal
from infrastructure.db.models.knowledge_model import TarotModel, AstrologyModel, NumerologyModel

def setup_database():
    print("--- Iniciando Oraculum Master Setup ---")
    
    # 1. Crear las tablas si no existen
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        # 2. Sembrar Tarot (Muestra de Arcanos)
        if not db.query(TarotModel).first():
            print("Sembrando Tarot...")
            tarot_data = [
                TarotModel(name="El Mago", meaning="Poder personal, iniciativa, accion.", keywords="Voluntad, Manifestacion"),
                TarotModel(name="La Sacerdotisa", meaning="Intuicion, misterio, sabiduria interior.", keywords="Inconsciente, Silencio"),
                TarotModel(name="La Torre", meaning="Cambio repentino, ruptura de estructuras.", keywords="Liberacion, Caos")
            ]
            db.add_all(tarot_data)

        # 3. Sembrar Astrologia
        if not db.query(AstrologyModel).first():
            print("Sembrando Astrologia...")
            astro_data = [
                AstrologyModel(name="Aries", category="Signo", element="Fuego", description="Energia de inicio, impulso y coraje."),
                AstrologyModel(name="Pluton", category="Planeta", element="Agua", description="Transformacion profunda, muerte y renacimiento.")
            ]
            db.add_all(astro_data)

        # 4. Sembrar Numerologia
        if not db.query(NumerologyModel).first():
            print("Sembrando Numerologia...")
            num_data = [
                NumerologyModel(number=1, vibration="Liderazgo", meaning="Individualidad y nuevos comienzos."),
                NumerologyModel(number=11, vibration="Maestro Espiritual", meaning="Iluminacion e intuicion superior.")
            ]
            db.add_all(num_data)

        db.commit()
        print("--- Setup completado con exito ---")
    except Exception as e:
        print(f"Error durante el setup: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    setup_database()
