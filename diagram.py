import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Configuração da figura
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Eixos de coordenadas
ax.quiver(0, 0, 0, 1, 0, 0, color='green', linestyle='-', linewidth=3, label='Transversal')
ax.quiver(0, 0, 0, 0, -1, 0, color='purple', linestyle='-', linewidth=3, label='Longitudinal')
ax.quiver(0, 0, 0, 0, 0, 1, color='yellow', linestyle='-', linewidth=3, label='Vertical')
ax.quiver(0, 0, 0, 0, 0, 1, color='red', linestyle='-', linewidth=1, label='Sustentação')
ax.quiver(0, 0, 0, 0, 1, 0, color='blue', linestyle='-', linewidth=1, label='Arrasto')

# Ajustando a exibição
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend(loc='upper left', fontsize=10)
ax.set_title('Esquema das Forças e Momentos em um Drone Quadrotor')

plt.savefig("diagram.png")
plt.show()