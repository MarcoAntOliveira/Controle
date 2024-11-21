import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Configuração da figura
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Eixos de coordenadas
ax.quiver(0, 0, 0, 1, 0, 0, color='black', linestyle='-', linewidth=3, label='Eixo X')
ax.quiver(0, 0, 0, 0, 1, 0, color='black', linestyle='-', linewidth=3, label='Eixo Y')
ax.quiver(0, 0, 0, 0, 0, 1, color='black', linestyle='-', linewidth=3, label='Eixo Z')

# Centro do drone
ax.scatter(0, 0, 0, color='black', s=50, label='Centro do Drone (B)')

# Posicionamento dos motores
motor_positions = [
    (1, 1, 0),  # Motor 1
    (-1, 1, 0),  # Motor 2
    (-1, -1, 0),  # Motor 3
    (1, -1, 0)   # Motor 4
]
forces = [
    (0, 0, 1),   # Força F1
    (0, 0, -1),   # Força F2
    (0, 0, 1),   # Força F3
    (0, 0, -1) ,   # Força F4
  
]
# Função para desenhar linhas curvas (momentos)

# Função para criar setas curvas indicando sentido de rotação
def draw_rotation_arrow(ax, center, radius, start_angle, end_angle, z_offset=0, direction='cw', color='blue'):
    # Define os ângulos
    theta = np.linspace(np.radians(start_angle), np.radians(end_angle), 100)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    z = np.full_like(x, center[2] + z_offset)  # Cria array constante para z

    # Adiciona linha curva
    ax.plot(x, y, z, color=color, linestyle='dashed', linewidth=2)
    
    # Posição da ponta da seta
    arrow_x = x[-1]
    arrow_y = y[-1]
    arrow_z = z[-1]

    # Direção da seta
    dx = x[-1] - x[-2]
    dy = y[-1] - y[-2]
    dz = z[-1] - z[-2]
    magnitude = (np.sqrt(dx**2 + dy**2 + dz**2))*5

    # Normaliza a direção da seta
    dx /= magnitude
    dy /= magnitude
    dz /= magnitude 

    # Ponta da seta
    ax.quiver(
        arrow_x, arrow_y, arrow_z, dx, dy, dz,
        color=color, arrow_length_ratio=0.5, linewidth=2
    )
def draw_rotation_arrow_x(ax, center, radius, start_angle, end_angle, x_offset=0, direction='cw', color='blue'):
    # Define os ângulos para a rotação no plano YZ
    theta = np.linspace(np.radians(start_angle), np.radians(end_angle), 100)
    y = center[1] + radius * np.cos(theta)  # Rotação no eixo Y
    z = center[2] + radius * np.sin(theta)  # Rotação no eixo Z
    x = np.full_like(y, center[0] + x_offset)  # Constante no eixo X

    # Adiciona linha curva
    ax.plot(x, y, z, color=color, linestyle='dashed', linewidth=2)
    
    # Posição da ponta da seta
    arrow_x = x[-1]
    arrow_y = y[-1]
    arrow_z = z[-1]

    # Direção da seta
    dy = y[-1] - y[-2]
    dz = z[-1] - z[-2]
    dx = x[-1] - x[-2]  # Será zero para rotação no plano YZ
    magnitude = np.sqrt(dx**2 + dy**2 + dz**2)*10

    # Normaliza a direção da seta
    dx /= magnitude
    dy /= magnitude
    dz /= magnitude

    # Ponta da seta
    ax.quiver(
        arrow_x, arrow_y, arrow_z, dx, dy, dz,
        color
        =color, arrow_length_ratio=0.5, linewidth=2
    )

# Rotação em torno do eixo Y
def draw_rotation_arrow_y(ax, center, radius, start_angle, end_angle, y_offset=0, color='green'):
    theta = np.linspace(np.radians(start_angle), np.radians(end_angle), 100)
    x = center[0] + radius * np.cos(theta)  # Rotação no eixo X
    z = center[2] + radius * np.sin(theta)  # Rotação no eixo Z
    y = np.full_like(x, center[1] + y_offset)  # Constante no eixo Y

    ax.plot(x, y, z, color=color, linestyle='dashed', linewidth=2)
    arrow_x, arrow_y, arrow_z = x[-1], y[-1], z[-1]
    dx, dy, dz = x[-1] - x[-2], 0, z[-1] - z[-2]
    magnitude = np.sqrt(dx**2 + dy**2 + dz**2) * 10
    dx, dy, dz = dx / magnitude, dy / magnitude, dz / magnitude
    ax.quiver(arrow_x, arrow_y, arrow_z, dx, dy, dz, color=color, arrow_length_ratio=0.5, linewidth=2)

# Rotação em torno do eixo Z
def draw_rotation_arrow_z(ax, center, radius, start_angle, end_angle, z_offset=0, color='red'):
    theta = np.linspace(np.radians(start_angle), np.radians(end_angle), 100)
    x = center[0] + radius * np.cos(theta)  # Rotação no eixo X
    y = center[1] + radius * np.sin(theta)  # Rotação no eixo Y
    z = np.full_like(x, center[2] + z_offset)  # Constante no eixo Z

    ax.plot(x, y, z, color=color, linestyle='dashed', linewidth=2)
    arrow_x, arrow_y, arrow_z = x[-1], y[-1], z[-1]
    dx, dy, dz = x[-1] - x[-2], y[-1] - y[-2], 0
    magnitude = np.sqrt(dx**2 + dy**2 + dz**2) * 10
    dx, dy, dz = dx / magnitude, dy / magnitude, dz / magnitude
    ax.quiver(arrow_x, arrow_y, arrow_z, dx, dy, dz, color=color, arrow_length_ratio=0.5, linewidth=2)



# Adicionando motores, forças e momentos
for i, pos in enumerate(motor_positions):
    # Motores
    ax.scatter(*pos, color='blue', s=70, label=f'Motor {i+1}')
    
    # Forças
    ax.quiver(*pos, *forces[i], color='red', linewidth=1, label=f'Força F{i+1}' )
    
    # Momentos
    if (i == 0 or i == 2):
        draw_rotation_arrow(ax, center=pos, radius=0.5, start_angle=0, end_angle=270, z_offset=0.1, 
                            direction="cw", color='blue')
        
    else:    
         draw_rotation_arrow(ax, center=pos, radius=0.5, start_angle=270, end_angle=0, z_offset=0.1, 
                            direction="ccw", color='blue')

# Vetores de rotação: Roll, Pitch, Yaw

pos_roll = (1, 0, 0)
ax.quiver(0, 0, 0, 1, 0, 0, color='green', linewidth=1.5, label='Roll (ϕ)')
draw_rotation_arrow_x(ax, center=(0.5, 0, 0), radius=0.25, start_angle=0, end_angle=300, x_offset=0.1, direction='cw', color='green')

ax.quiver(0, 0, 0, 0, 1, 0, color='orange', linewidth=1.5, label='Pitch (θ)')

draw_rotation_arrow_y(ax, center=(0, 0.5, 0), radius=0.25, start_angle=0, end_angle=300, y_offset=0.1,  color='orange')

ax.quiver(0, 0, 0, 0, 0, 1, color='purple', linewidth=1.5, label='Yaw (ψ)')

draw_rotation_arrow_z(ax, center=(0, 0, 0.5), radius=0.25, start_angle=0, end_angle=300, z_offset=0.1, color='purple')

ax.quiver(0, 0, 0, 0, 0, -1, color='pink', linewidth=1.5, label='weight')

# Ajustando a exibição
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([0, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend(loc='upper left', fontsize=10)
ax.set_title('Esquema das Forças e Momentos em um Drone Quadrotor')

plt.savefig("diagram.png")
plt.show()


