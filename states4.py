import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Função para criar setas curvas indicando sentido de rotação
def draw_rotation_arrow(ax, center, radius, start_angle, end_angle, z_offset=0, direction='cw', color='blue'):
    # Define os ângulos
    theta = np.linspace(np.radians(start_angle), np.radians(end_angle), 100)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    z = np.full_like(x, center[2] + z_offset)  # Cria array constante para z

    # Adiciona linha curva
    ax.plot(x, y, z, color=color, linestyle='solid', linewidth=2)
    
    # Posição da ponta da seta
    arrow_x = x[-1]
    arrow_y = y[-1]
    arrow_z = z[-1]

    # Direção da seta
    dx = x[-1] - x[-2]
    dy = y[-1] - y[-2]
    dz = z[-1] - z[-2]
    magnitude = np.sqrt(dx**2 + dy**2 + dz**2)

    # Normaliza a direção da seta
    dx /= magnitude
    dy /= magnitude
    dz /= magnitude

    # Ponta da seta
    ax.quiver(
        arrow_x, arrow_y, arrow_z, dx, dy, dz,
        color=color, arrow_length_ratio=0.1, linewidth=2
    )

# Configuração da figura
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Centro do drone
ax.scatter(0, 0, 0, color='black', s=50, label='Centro do Drone (B)')

# Motores e posições
motor_positions = [
    (1, 1, 0),  # Motor 1
    (-1, 1, 0),  # Motor 2
    (-1, -1, 0),  # Motor 3
    (1, -1, 0)   # Motor 4
]
rotations = ['cw', 'ccw', 'cw', 'ccw']  # Sentido de rotação: horário (cw) e anti-horário (ccw)

# Adicionando setas para o sentido de rotação
for i, pos in enumerate(motor_positions):
    draw_rotation_arrow(ax, center=pos, radius=0.5, start_angle=0, end_angle=270, z_offset=0.1, 
                        direction=rotations[i], color='blue')

# Adicionando Eixos
ax.quiver(0, 0, 0, 1, 0, 0, color='black', linestyle='-', linewidth=2, label='Eixo X')
ax.quiver(0, 0, 0, 0, 1, 0, color='black', linestyle='-', linewidth=2, label='Eixo Y')
ax.quiver(0, 0, 0, 0, 0, 1, color='black', linestyle='-', linewidth=2, label='Eixo Z')

# Ajustando a exibição
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([0, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend(loc='upper left', fontsize=10)
ax.set_title('Esquema com Sentido de Rotação dos Motores')

plt.show()
