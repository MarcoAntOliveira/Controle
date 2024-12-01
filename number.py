import numpy as np
import matplotlib.pyplot as plt
from control import tf, pole

# Parâmetros
Kp = 2  # Ganho proporcional fixo
zeta_values = np.linspace(0, 5, 200)  # Valores de ζ (200 amostras entre 0 e 5)

# Inicialização do gráfico
plt.figure(figsize=(10, 6))
plt.title("Lugar das Raízes em função de ζ (0 ≤ ζ < ∞)")
plt.xlabel("Parte Real")
plt.ylabel("Parte Imaginária")
plt.axhline(0, color='k', linestyle='--', linewidth=0.7)  # Eixo imaginário
plt.axvline(0, color='k', linestyle='--', linewidth=0.7)  # Eixo real
plt.grid()

# Loop para calcular os pólos para diferentes valores de ζ
for zeta in zeta_values:
    # Definição da função de transferência
    num = [4 * Kp]  # Numerador: 4 * Kp
    den = [1, 4 * zeta, 4 + 4 * Kp]  # Denominador: s^2 + 4ζs + (4 + 4Kp)
    system = tf(num, den)
    
    # Calcula os pólos do sistema
    poles = pole(system)
    
    # Adiciona os pólos ao gráfico
    plt.plot(poles.real, poles.imag, 'b.', markersize=2)

# Mostra o gráfico
plt.show()
