import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class TrafficLightController:
    def __init__(self, target_flow, Kp, Ki, Kd):
        self.target_flow = target_flow
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.integral = 0
        self.previous_error = 0
        self.traffic_light_duration = 30  # Duração inicial do semáforo verde (com PID)

    def update_flow(self, current_flow, dt):
        error = self.target_flow - current_flow
        self.integral += error * dt
        derivative = (error - self.previous_error) / dt

        # Controle PID
        adjustment = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.traffic_light_duration = max(10, min(90, self.traffic_light_duration + adjustment))  # Limita entre 10 e 90s

        self.previous_error = error
        return self.traffic_light_duration

# Função que simula um padrão de tráfego (carros/minuto)
def traffic_pattern(t):
    base_flow = 20
    rush_hour_increase = 30 if 8 <= t % 24 <= 10 or 17 <= t % 24 <= 19 else 0
    return base_flow + rush_hour_increase + np.random.normal(0, 5)

# Configurações da simulação
target_flow = 30
Kp = 0.5
Ki = 0.1
Kd = 0.05
time_steps = 1440  # Simulação de 24 horas em minutos

# Inicializa o controlador
controller = TrafficLightController(target_flow, Kp, Ki, Kd)

# Dados para o gráfico
time_data = []
flow_data = []
duration_data_pid = []
duration_data_fixed = []

# Configurações do gráfico
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Gráfico com PID
line_pid, = ax1.plot([], [], label="Duração do Semáforo (PID)", color='green')
flow_pid, = ax1.plot([], [], label="Fluxo de Carros (com PID)", color='red', linestyle='--')
ax1.set_title("Ajuste do Semáforo Verde (com PID) e Fluxo de Carros")
ax1.set_xlabel("Tempo (minutos)")
ax1.set_ylabel("Duração do Semáforo (segundos) / Fluxo de Carros")
ax1.grid(True)
ax1.legend()

# Gráfico sem PID
line_fixed, = ax2.plot([], [], label="Duração do Semáforo (sem PID)", color='blue')
flow_fixed, = ax2.plot([], [], label="Fluxo de Carros (sem PID)", color='orange', linestyle='--')
ax2.set_title("Semáforo Verde Fixo (sem PID) e Fluxo de Carros")
ax2.set_xlabel("Tempo (minutos)")
ax2.set_ylabel("Duração do Semáforo (segundos) / Fluxo de Carros")
ax2.grid(True)
ax2.legend()

# Limites do gráfico
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 100)
ax2.set_xlim(0, 100)
ax2.set_ylim(0, 100)

# Função de inicialização para o gráfico
def init():
    line_pid.set_data([], [])
    flow_pid.set_data([], [])
    line_fixed.set_data([], [])
    flow_fixed.set_data([], [])
    return line_pid, flow_pid, line_fixed, flow_fixed

# Função de animação
def update(frame):
    global time_data, flow_data, duration_data_pid, duration_data_fixed

    # Simulação de tráfego e controle PID
    current_flow = traffic_pattern(frame)
    current_duration_pid = controller.update_flow(current_flow, 1)
    current_duration_fixed = 30  # Sem controle PID, tempo fixo

    # Armazenar dados
    time_data.append(frame)
    flow_data.append(current_flow)
    duration_data_pid.append(current_duration_pid)
    duration_data_fixed.append(current_duration_fixed)

    # Limitar os dados para o gráfico em tempo real (mostrar últimos 100 pontos)
    if len(time_data) > 100:
        time_data = time_data[-100:]
        duration_data_pid = duration_data_pid[-100:]
        duration_data_fixed = duration_data_fixed[-100:]
        flow_data = flow_data[-100:]

    # Atualizar os dados da linha do gráfico
    line_pid.set_data(time_data, duration_data_pid)
    flow_pid.set_data(time_data, flow_data)

    line_fixed.set_data(time_data, duration_data_fixed)
    flow_fixed.set_data(time_data, flow_data)

    ax1.set_xlim(max(0, frame - 100), frame)
    ax2.set_xlim(max(0, frame - 100), frame)
    
    return line_pid, flow_pid, line_fixed, flow_fixed

# Executa a animação
ani = FuncAnimation(fig, update, frames=np.arange(0, time_steps), init_func=init, blit=True, interval=100, repeat=False)

plt.tight_layout()
plt.show()
