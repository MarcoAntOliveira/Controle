import numpy as np

# Coeficientes da equação quadrática para os polos
a = 0.2
b = 2.1

# Função corrigida para lidar com discriminantes negativos e retornar polos complexos
def calcular_polos_corrigido(Kp):
    c = 1 + 10 * Kp
    discriminant = b**2 - 4 * a * c
    if discriminant >= 0:
        # Polos reais
        s1 = (-b + np.sqrt(discriminant)) / (2 * a)
        s2 = (-b - np.sqrt(discriminant)) / (2 * a)
    else:
        # Polos complexos
        real_part = -b / (2 * a)
        imag_part = np.sqrt(-discriminant) / (2 * a)
        s1 = complex(real_part, imag_part)
        s2 = complex(real_part, -imag_part)
    return s1, s2

# Calculando polos corrigidos para os valores de Kp
Kp_values = [1, 5, 10, 20, 50]
poles_corrected = [calcular_polos_corrigido(Kp) for Kp in Kp_values]
poles_corrected
    