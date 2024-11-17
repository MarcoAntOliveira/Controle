import matplotlib.pyplot as plt
import numpy as np

# Configuração inicial
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')

# Corpo do drone (uma cruz)
ax.plot([-1, 1], [0, 0], color='black', lw=2, label='Corpo do Drone')  # Braço horizontal
ax.plot([0, 0], [-1, 1], color='black', lw=2)  # Braço vertical

# Motores (círculos nas extremidades)
motor_positions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for x, y in motor_positions:
    motor_circle = plt.Circle((x, y), 0.1, color='blue', ec='black', label='Motor' if (x, y) == (1, 0) else None)
    ax.add_patch(motor_circle)

# Forças geradas pelos motores
for x, y in motor_positions:
    ax.arrow(x, y, 0, 0.5 if y >= 0 else -0.5, head_width=0.1, head_length=0.1, fc='red', ec='red', label='Força (Tração)' if y == 1 else None)

# Vetores de torque (exemplo simplificado)
ax.arrow(0, 0, 0.7, -0.7, head_width=0.1, head_length=0.1, fc='green', ec='green', label='Torque')

# Personalização
ax.set_title('Esquema do Movimento de um Drone')
ax.axhline(0, color='gray', lw=0.5, linestyle='--')
ax.axvline(0, color='gray', lw=0.5, linestyle='--')
ax.legend(loc='upper left', fontsize=10)

# Mostrar
plt.grid()
plt.show()
