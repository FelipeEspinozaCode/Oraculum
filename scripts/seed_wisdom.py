from infrastructure.db.session import SessionLocal
from infrastructure.db.models.knowledge_model import TarotModel, NumerologyModel, AstrologyModel

def seed_wisdom():
    db = SessionLocal()
    try:
        # --- TAROT: 22 ARCANOS MAYORES (Campo: arcane_type) ---
        tarot_data = [
            ("El Loco", "Nuevos comienzos, fe, espontaneidad.", "Inocencia, Salto"),
            ("El Mago", "Poder personal, voluntad, creación.", "Acción, Herramientas"),
            ("La Sacerdotisa", "Intuición, misterio, voz interior.", "Inconsciente, Silencio"),
            ("La Emperatriz", "Abundancia, maternidad, naturaleza.", "Creatividad, Fertilidad"),
            ("El Emperador", "Estructura, autoridad, orden.", "Control, Estabilidad"),
            ("El Hierofante", "Tradición, guía espiritual, valores.", "Sabiduría, Mentor"),
            ("Los Enamorados", "Elecciones, amor, alineación.", "Valores, Unión"),
            ("El Carro", "Determinación, victoria, control.", "Éxito, Dirección"),
            ("La Justicia", "Equidad, verdad, ley.", "Causa y Efecto, Integridad"),
            ("El Ermitaño", "Introspección, soledad, luz.", "Sabiduría, Retiro"),
            ("La Rueda de la Fortuna", "Ciclos, destino, cambio.", "Evolución, Suerte"),
            ("La Fuerza", "Coraje, suavidad, autocontrol.", "Domar instintos, Valor"),
            ("El Colgado", "Nueva perspectiva, pausa, entrega.", "Iluminación, Sacrificio"),
            ("La Muerte", "Transformación, final, renacer.", "Transmutación, Cambio profundo"),
            ("La Templanza", "Moderación, equilibrio, alquimia.", "Paciencia, Mezcla"),
            ("El Diablo", "Apego, sombra, materialismo.", "Esclavitud, Tentación"),
            ("La Torre", "Cambio súbito, revelación, liberación.", "Ruptura, Despertar"),
            ("La Estrella", "Esperanza, inspiración, fe.", "Sanación, Destino"),
            ("La Luna", "Miedo, ilusión, inconsciente.", "Sueños, Intuición sombría"),
            ("El Sol", "Éxito, vitalidad, alegría.", "Claridad, Verdad"),
            ("El Juicio", "Despertar, llamado, absolución.", "Evaluación, Renacimiento"),
            ("El Mundo", "Integración, logro, plenitud.", "Cierre de ciclo, Éxito total")
        ]

        # --- NUMEROLOGÍA (Campos: number, vibration, meaning) ---
        num_data = [
            (1, "El Iniciador", "Individualidad, independencia y coraje."),
            (2, "El Mediador", "Dualidad, cooperación y sensibilidad."),
            (3, "El Comunicador", "Expresión creativa, optimismo y vida social."),
            (4, "El Constructor", "Trabajo duro, orden, lealtad y cimientos."),
            (5, "El Viajero", "Libertad, aventura y adaptabilidad."),
            (6, "El Nutridor", "Responsabilidad, amor familiar y armonía."),
            (7, "El Analista", "Espiritualidad, estudio y perfeccionamiento."),
            (8, "El Ejecutivo", "Poder material, éxito financiero y karma."),
            (9, "El Humanitario", "Compasión, cierres de ciclo y sabiduría."),
            (11, "El Iluminador", "Intuición maestra y visión espiritual."),
            (22, "El Maestro Constructor", "Manifestación de grandes proyectos."),
            (33, "El Guía Espiritual", "Servicio incondicional y amor universal.")
        ]

        # --- ASTROLOGÍA (Campos: name, category, element, description) ---
        astro_data = [
            ("Sol", "Planeta", "Fuego", "El centro del ser, la identidad."),
            ("Luna", "Planeta", "Agua", "Las emociones y el mundo interno."),
            ("Aries", "Signo", "Fuego", "Energía de inicio y valentía."),
            ("Tauro", "Signo", "Tierra", "Persistencia y valor material."),
            ("Geminis", "Signo", "Aire", "Dualidad y curiosidad mental."),
            ("Cancer", "Signo", "Agua", "Nutrición emocional y hogar."),
            ("Leo", "Signo", "Fuego", "Expresión y centro de atención."),
            ("Virgo", "Signo", "Tierra", "Análisis y servicio detallado."),
            ("Libra", "Signo", "Aire", "Armonía y relaciones."),
            ("Escorpio", "Signo", "Agua", "Intensidad y transmutación."),
            ("Sagitario", "Signo", "Fuego", "Expansión y búsqueda de verdad."),
            ("Capricornio", "Signo", "Tierra", "Ambición y responsabilidad."),
            ("Acuario", "Signo", "Aire", "Innovación y desapego."),
            ("Piscis", "Signo", "Agua", "Empatía y conexión espiritual.")
        ]

        # Inserción masiva corregida
        for n, m, k in tarot_data:
            if not db.query(TarotModel).filter_by(name=n).first():
                db.add(TarotModel(name=n, meaning=m, keywords=k, arcane_type="Mayor"))

        for num, vib, mean in num_data:
            if not db.query(NumerologyModel).filter_by(number=num).first():
                db.add(NumerologyModel(number=num, vibration=vib, meaning=mean))

        for n, cat, el, desc in astro_data:
            if not db.query(AstrologyModel).filter_by(name=n).first():
                db.add(AstrologyModel(name=n, category=cat, element=el, description=desc))

        db.commit()
        print("✅ SABIDURÍA ANCESTRAL CARGADA (Tarot 22, Números 12, Astros 14).")
    except Exception as e:
        db.rollback()
        print(f"❌ Error en siembra: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_wisdom()
