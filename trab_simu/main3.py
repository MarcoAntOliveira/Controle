
import control as ct
import numpy as np
import matplotlib.pyplot as plt
from functions import routh_hurwitz, plot_root_locus
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti, step
servo = ct.TransferFunction([-1], [1, 10])  # Servo do elevador
dynamics = ct.TransferFunction([-2.0, -0.6], [1, 0.65, 2.15, 0])  # Dinâmica de curto período
open_loop = servo * dynamics  # Função de transferência em malha aberta
Kp_range = np.linspace(1, 1000, 2000)  # Ganhos de 1 a 1000

t_sim = 20  # Tempo de simulação (s)


out_st_magn = ct.stability_margins(open_loop)
Ku = out_st_magn[0]
print(Ku)

Wu = out_st_magn[3]
Tu = (2*np.pi)/Wu

print(Tu)

# try:
#     Ku, Tu = find_critical_gain_and_period(open_loop, Kp_range, t_sim)
#     print(f"Ganho crítico (Ku): {Ku}")
#     print(f"Período crítico (Tu): {Tu}")
# except ValueError as e:
#     print(str(e))
#     Ku, Tu = None, None  # Garantia para não usar valores indefinidos

# try:
#     Ku, Tu = find_critical_gain_and_period_1(open_loop, Kp_range, t_sim)
#     print(f"Ganho crítico (Ku): {Ku}")
#     print(f"Período crítico (Tu): {Tu}")
# except ValueError as e:
#     print(str(e))
#     Ku, Tu = None, None  # Garantia para não usar valores indefinidos



# Plot da malha fechada para Ku, se encontrado
if Ku is not None:
    controller = ct.TransferFunction([Ku], [1])
    closed_loop = ct.feedback(controller * open_loop)

    t = np.linspace(0, t_sim, 1000)
    t, y = ct.step_response(closed_loop, t)

    plt.figure()
    plt.plot(t, y)
    plt.title("Closed Loop Response with Critical Gain (Ku)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.savefig("response_ku.png")
    plt.show()

# Definir os parâmetros dos controladores
if Ku is not None:
    Kp_P = 0.5 * Ku
    print(f"o ganho proporcional{Kp_P}")
    Kp_PI = 0.45 * Ku
    Ki_PI = Tu / 1.2
    print(f'o ganho proporcional{Kp_PI} e o ganho integrativo é {Ki_PI}')
    Kp_PID = 0.68 * Ku
    Ki_PID = Tu / 2
    Kd_PID = Tu * 0.125
    print(f'o ganho proporcional{Kp_PID} e o ganho integrativo é {Ki_PID} e o ganho derivativo é {Kd_PID}')

    # Criar funções de transferência com os controladores
    numerator = [3]
    denominator = [1, 12, 25, 50]

    system_P = lti([Kp_P * n for n in numerator], denominator)
    system_PI = lti([Kp_PI * n for n in numerator], np.convolve(denominator, [1, Ki_PI]))
    system_PID = lti([Kd_PID, Kp_PID, Ki_PID], denominator)
        # Encontrar o valor do pico (ressalto)
    

    # Erro em estado estacionário (diferença entre valor final e o desejado)
    

    # Tempo para simulação
    time = np.linspace(0, 20, 1000)

    # Respostas no tempo
    _, response_P = step(system_P, T=time)
    _, response_PI = step(system_PI, T=time)
    _, response_PID = step(system_PID, T=time)
# Encontrar o valor do pico (ressalto)
overshoot_p = np.max(response_P) - 1  # Ressalto para sistema P
overshoot_pi = np.max(response_PI) - 1  # Ressalto para sistema PI
overshoot_pid = np.max(response_PID) - 1  # Ressalto para sistema PID

print(f"O ressalto (overshoot) para P: {overshoot_p}")
print(f"O ressalto (overshoot) para PI: {overshoot_pi}")
print(f"O ressalto (overshoot) para PID: {overshoot_pid}")

# Calcular erro em estado estacionário (diferença entre o valor final e o desejado 1)
steady_state_error_p = abs(response_P[-1] - 1)
steady_state_error_pi = abs(response_PI[-1] - 1)
steady_state_error_pid = abs(response_PID[-1] - 1)

print(f"Erro em estado estacionário (P): {steady_state_error_p}")
print(f"Erro em estado estacionário (PI): {steady_state_error_pi}")
print(f"Erro em estado estacionário (PID): {steady_state_error_pid}")

# Calcular os elementos de Bode Plot para cada sistema
omega, mag_P, phase_P = ct.bode(system_P, plot=False)
omega, mag_PI, phase_PI = ct.bode(system_PI, plot=False)
omega, mag_PID, phase_PID = ct.bode(system_PID, plot=False)

# Plotar Magnitude
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.semilogx(omega, 20 * np.log10(mag_P), label='Sistema P')
plt.semilogx(omega, 20 * np.log10(mag_PI), label='Sistema PI')
plt.semilogx(omega, 20 * np.log10(mag_PID), label='Sistema PID')

plt.title("Magnitude do Diagrama de Bode")
plt.xlabel("Frequência (rad/s)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)
plt.legend()

# Plotar Fase
plt.subplot(2, 1, 2)
plt.semilogx(omega, np.degrees(phase_P), label='Sistema P')
plt.semilogx(omega, np.degrees(phase_PI), label='Sistema PI')
plt.semilogx(omega, np.degrees(phase_PID), label='Sistema PID')

plt.title('Diagrama de Fase')
plt.xlabel('Frequência (rad/s)')
plt.ylabel('Fase (graus)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
