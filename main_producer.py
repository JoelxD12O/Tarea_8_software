from datetime import datetime
from src.domain.entities.consumption import Consumption
from src.infrastructure.messaging.rabbitmq_adapter import RabbitMQAdapter
from src.application.use_cases.register_consumption import RegisterConsumptionUseCase

def main():
    # Credenciales del enunciado
    HOST = "213.199.42.57"
    PORT = 5672
    USER = "students"
    PASS = "Ut3c2026"
    
    adapter = RabbitMQAdapter(HOST, PORT, USER, PASS)
    use_case = RegisterConsumptionUseCase(adapter)
    
    # Simular un registro de consumo
    nuevo_consumo = Consumption(
        amount=150.50,
        card_number="4557-1234-5678-9012",
        restaurant_id="Restaurante_UTEC_01",
        timestamp=datetime.now()
    )
    
    print(f"[*] Registrando consumo por ${nuevo_consumo.amount}...")
    use_case.execute(nuevo_consumo)
    print("[x] Registro enviado al broker exitosamente.")

if __name__ == "__main__":
    main()
