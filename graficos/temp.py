import numpy as np
from math import sqrt

# Coeficientes da equação quadrática para os polos
a = 0.2
b = 2.1

# Função para calcular os polos para um dado Kp
def calcular_polos(Kp):
    c = 1 + 10 * Kp
    # Fórmula para calcular os polos
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        parte_real = -b / (2*a)
        parte_imaginaria = sqrt(-discriminant) / (2*a)
        x1 = complex(parte_real, parte_imaginaria)
        x2 = complex(parte_real, -parte_imaginaria)
        return x1, x2
        
    elif(discriminant> 0):    
        s1 = (-b + np.sqrt(discriminant)) / (2 * a)
        s2 = (-b - np.sqrt(discriminant)) / (2 * a)
        return s1, s2
    else:
        return  -b / (2*a)
        
        

# Valores de Kp para análise
Kp_values = [1, 5, 10, 20, 50]
poles = [calcular_polos(Kp) for Kp in Kp_values]

# Exibindo os polos para cada valor de Kp
poles
