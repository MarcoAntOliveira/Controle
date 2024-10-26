import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parâmetros do circuito
R = 1e3  # resistência em ohms
C = 1e-6  # capacitância em farads
tau = R * C  # constante de tempo do sistema

# Função para a derivada de vc(t) de acordo com a EDO: dvc/dt = (vi - vc) / (R * C)
def rc_circuit(t, vc, vi):
    return (vi - vc) / (R * C)

# Configuração do tempo de simulação
t_final = 0.05  # tempo final em segundos
t = np.linspace(0, t_final, 1000)  # vetor de tempo

# Primeira situação: vc(0) = 0 V, vi(t) = 10 V
vi_1 = 10  # tensão de entrada
vc0_1 = 0  # condição inicial para vc(t)
sol_1 = solve_ivp(rc_circuit, [0, t_final], [vc0_1], args=(vi_1,), t_eval=t)

# Segunda situação: vc(0) = 5 V, vi(t) = 10 V
vc0_2 = 5  # condição inicial para vc(t)
sol_2 = solve_ivp(rc_circuit, [0, t_final], [vc0_2], args=(vi_1,), t_eval=t)

# Plotando os resultados
plt.figure(figsize=(10, 6))
plt.plot(sol_1.t, sol_1.y[0], label='vc(t) para vc(0) = 0V', color='blue')
plt.plot(sol_2.t, sol_2.y[0], label='vc(t) para vc(0) = 5V', color='red')
plt.xlabel("Tempo (s)")
plt.ylabel("Tensão no capacitor vc(t) (V)")
plt.title("Resposta do sistema RC para diferentes condições iniciais")
plt.legend()
plt.grid()
plt.show()
