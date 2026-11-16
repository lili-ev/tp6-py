
from dataclasses import dataclass, asdict
import json


@dataclass(frozen=True, slots=True)
class Film:
    titre: str
    realisateur: str
    annee: int
    note: float

    def __post_init__(self):
        if not isinstance(self.titre, str) or not self.titre.strip():
            raise ValueError("Le titre doit être une chaîne non vide.")

        if not isinstance(self.realisateur, str) or not self.realisateur.strip():
            raise ValueError("Le réalisateur doit être une chaîne non vide.")

        if type(self.annee) is not int:
            raise TypeError("L'année doit être un entier.")

        if type(self.note) not in (int, float):
            raise TypeError("La note doit être un nombre.")

        if not 0 <= self.note <= 10:
            raise ValueError("La note doit être comprise entre 0 et 10.")

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    def est_classique(self):
        return self.annee < 2000
