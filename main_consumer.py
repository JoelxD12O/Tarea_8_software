from src.infrastructure.messaging.rabbitmq_adapter import RabbitMQAdapter
from src.application.use_cases.process_rewards import ProcessRewardsUseCase

def main():
    # Credenciales del enunciado
    HOST = "213.199.42.57"
    PORT = 5672
    USER = "students"
    PASS = "Ut3c2026"
    
    adapter = RabbitMQAdapter(HOST, PORT, USER, PASS)
    rewards_use_case = ProcessRewardsUseCase()
    
    def on_consumption_received(consumption):
        rewards_use_case.execute(consumption)

    print("[*] Iniciando sistema de Recompensas (Consumidor)...")
    adapter.start_consuming(on_consumption_received)

if __name__ == "__main__":
    main()
