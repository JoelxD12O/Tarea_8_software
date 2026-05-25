from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class Consumption:
    amount: float
    card_number: str
    restaurant_id: str
    timestamp: datetime

    def calculate_points(self) -> int:
        # Ejemplo: 1 punto por cada 10 unidades monetarias
        return int(self.amount // 10)

    def calculate_cashback(self) -> float:
        # Ejemplo: 2% de cashback
        return round(self.amount * 0.02, 2)
