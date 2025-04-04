import control as ct
import numpy as np
import matplotlib.pyplot as plt

# Planta de 2ª ordem
dynamics = ct.TransferFunction([1], [1, 2, 10])
open_loop = dynamics

# Parâmetros críticos
out_st_magn = ct.stability_margins(open_loop)
Ku = out_st_magn[0]
Wu = out_st_magn[3]

if Ku is None or Wu is None or Ku == 0 or np.isnan(Wu):
    print("Erro: não foi possível calcular Ku ou Wu. Verifique a função de transferência.")
    exit()

Tu = (2 * np.pi) / Wu

# Ganhos PID (Ziegler–Nichols)
Kp_P = 0.5 * Ku
Kp_PI = 0.45 * Ku
Ki_PI = Kp_PI / (Tu / 1.2)
Kp_PID = 0.68 * Ku
Ki_PID = Kp_PID / (Tu / 2)
Kd_PID = Kp_PID * (Tu * 0.125)

print(f"Kp: {Kp_P}")
print(f"Kp_PI: {Kp_PI}, Ki_PI: {Ki_PI}")
print(f"Kp_PID: {Kp_PID}, Ki_PID: {Ki_PID}, Kd_PID: {Kd_PID}")

# Controladores
P = ct.TransferFunction([Kp_P], [1])
PI = ct.TransferFunction([Kp_PI, Ki_PI], [1, 0])
PID = ct.TransferFunction([Kd_PID, Kp_PID, Ki_PID], [1, 0])

# Sistemas em malha fechada
system_P = ct.feedback(P * open_loop)
system_PI = ct.feedback(PI * open_loop)
system_PID = ct.feedback(PID * open_loop)

# Resposta ao degrau
time = np.linspace(0, 20, 1000)
t_P, response_P = ct.step_response(system_P, T=time)
t_PI, response_PI = ct.step_response(system_PI, T=time)
t_PID, response_PID = ct.step_response(system_PID, T=time)

# Análise
print(f"Overshoot P: {np.max(response_P) - 1}")
print(f"Overshoot PI: {np.max(response_PI) - 1}")
print(f"Overshoot PID: {np.max(response_PID) - 1}")

print(f"Erro estacionário P: {abs(response_P[-1] - 1)}")
print(f"Erro estacionário PI: {abs(response_PI[-1] - 1)}")
print(f"Erro estacionário PID: {abs(response_PID[-1] - 1)}")

# Gráfico comparativo
plt.figure(figsize=(10, 6))
plt.plot(t_P, response_P, label='P')
plt.plot(t_PI, response_PI, label='PI')
plt.plot(t_PID, response_PID, label='PID')
plt.axhline(1, color='k', linestyle='--', linewidth=0.7)
plt.title("Respostas ao Degrau para P, PI, PID")
plt.xlabel("Tempo (s)")
plt.ylabel("Saída")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
