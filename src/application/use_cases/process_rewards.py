from src.domain.entities.consumption import Consumption

class ProcessRewardsUseCase:
    def execute(self, consumption: Consumption) -> dict:
        points = consumption.calculate_points()
        cashback = consumption.calculate_cashback()
        
        # Aquí iría la lógica para persistir en una base de datos de recompensas
        print(f"[*] Procesando recompensas para tarjeta {consumption.card_number}")
        print(f"    - Puntos ganados: {points}")
        print(f"    - Cashback: ${cashback}")
        
        return {
            "status": "success",
            "points": points,
            "cashback": cashback
        }
