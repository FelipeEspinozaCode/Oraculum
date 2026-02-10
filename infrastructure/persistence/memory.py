from typing import Dict, List
from app.schemas.oracle import OracleInterpretation


class ReadingRepository:
    """
    Repositorio en memoria con soporte multi-tenant.
    Cada usuario tiene su propio historial.
    """

    def __init__(self) -> None:
        self._storage: Dict[str, List[OracleInterpretation]] = {}

    def save_for_user(self, owner_id: str, reading: OracleInterpretation) -> None:
        if owner_id not in self._storage:
            self._storage[owner_id] = []
        self._storage[owner_id].append(reading)

    def list_by_user(self, owner_id: str) -> List[OracleInterpretation]:
        return self._storage.get(owner_id, [])
