from infrastructure.db.session import SessionLocal
from infrastructure.db.models.knowledge_model import TarotModel, AstrologyModel, NumerologyModel
from services.utils.matcher import symbolic_match

class SymbolicInterpreter:
    def interpret(self, semantic_data: any, user_id: str = None):
        db = SessionLocal()
        domain = semantic_data.domain.value if hasattr(semantic_data.domain, 'value') else str(semantic_data.domain)
        symbols = semantic_data.symbols
        results = []

        try:
            if domain == "astrology":
                items = db.query(AstrologyModel).all()
                names = [i.name for i in items]
                for s in symbols:
                    match_name = symbolic_match(s, names)
                    if match_name:
                        res = next((i for i in items if i.name == match_name), None)
                        if res and not any(r['symbol'] == res.name for r in results):
                            results.append({"symbol": res.name, "meaning": res.description, "type": "astrology"})

            elif domain == "tarot":
                items = db.query(TarotModel).all()
                names = [i.name for i in items]
                for s in symbols:
                    match_name = symbolic_match(s, names)
                    if match_name:
                        res = next((i for i in items if i.name == match_name), None)
                        if res and not any(r['symbol'] == res.name for r in results):
                            results.append({"symbol": res.name, "meaning": res.meaning, "type": "tarot"})

            elif domain == "numerology":
                for s in symbols:
                    num_val = int(s) if str(s).isdigit() else 0
                    res = db.query(NumerologyModel).filter(NumerologyModel.number == num_val).first()
                    if res:
                        results.append({"symbol": str(res.number), "meaning": res.meaning, "type": "numerology"})

            return results
        finally:
            db.close()
