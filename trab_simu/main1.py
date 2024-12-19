import control as ct
import numpy as np
import matplotlib.pyplot as plt
from functions import routh_hurwitz, plot_root_locus
import numpy as np
import matplotlib.pyplot as plt





den_servo = [1, 10]
num_servo = [-1]
den_dynamics = [1, 0.65, 2.15]
num_dynamics = [-2.0, -0.6]


# Definição das funções de transferência
servo = ct.TransferFunction(num_servo, den_servo)  # Servo do elevador
dynamics = ct.TransferFunction([-2.0, -0.6], [1, 0.65, 2.15])  # Dinâmica de curto e malha

# Função de transferência em malha aberta
open_loop = servo * dynamics

# Obtém a resposta ao degrau
time, response = ct.step_response(open_loop)

# # Plotar a resposta ao degrau
# plt.figure(figsize=(10, 6))
# plt.plot(time, response)
# plt.title('Resposta ao Degrau')
# plt.xlabel('Tempo [s]')
# plt.ylabel('Amplitude')
# plt.grid(True)
# plt.savefig("step_response.png")  # Salva como PNG
# plt.show()


# Calcular métricas robustas
overshoot = max(response) - 1  # Sobresalto em relação ao valor desejado 1
steady_state_error = abs(response[-1] - 1)  # Erro em estado estacionário

# Usar interpolação linear para estimar o tempo de subida aproximado
target = 0.7  # Valor desejado
indices_above_target = np.where(response >= target)[0]

if len(indices_above_target) > 0:
    time_to_rise = time[indices_above_target[0]]
    print(f'Tempo de Subida aproximado (Interpolação): {time_to_rise:.2f} segundos')
else:
    time_to_rise = float('inf')  # Caso não atinja 0.9
    print('Resposta não atinge o valor desejado de tempo de subida (0.9)')

print(f'Sobresalto: {overshoot:.2f}')
print(f'Erro em estado estacionário: {steady_state_error:.4f}')
print(f'Tempo de Subida aproximado (Interpolação): {time_to_rise:.2f} segundos')

# print(routh_hurwitz(num_dynamics))

# plot_root_locus(open_loop)

# Bode plot para malha aberta
plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
mag, phase, omega = ct.bode_plot(open_loop, dB=True, plot=False)
plt.semilogx(omega, 20 * np.log10(mag))
plt.title("Bode Plot - Open Loop")
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Magnitude (dB)")

plt.grid()
plt.subplot(2, 1, 2)
plt.semilogx(omega, phase)
plt.title("Bode Plot - Open Loop")
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Phase (rad)")
plt.grid()
plt.tight_layout()
plt.savefig("bode_diagram.png")
plt.show()