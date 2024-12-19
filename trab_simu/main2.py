import numpy as np
import matplotlib.pyplot as plt
import control as ct
from scipy.signal import lti, step

# Definição da planta
servo = ct.TransferFunction([-1], [1, 10])  
dynamics = ct.TransferFunction([-2.0, -0.6], [1, 0.65, 2.15])  
open_loop = servo * dynamics  

Kp_range = np.linspace(1, 500, 1000)  
t_sim = 20  

# Determina Ku e Tu
def find_critical_gain_and_period(open_loop, Kp_range, t_sim):
    for Kp in Kp_range:
        controller = ct.TransferFunction([Kp], [1])
        closed_loop = ct.feedback(controller * open_loop)
        t = np.linspace(0, t_sim, 1000)
        _, y = ct.step_response(closed_loop, t)
        if np.max(y) > 1.5:
            return Kp, t[np.argmax(y)]
    raise ValueError("Ganho crítico não encontrado no intervalo fornecido.")

try:
    Ku, Tu = find_critical_gain_and_period(open_loop, Kp_range, t_sim)
    print(f"Ganho crítico (Ku): {Ku}")
    print(f"Período crítico (Tu): {Tu}")
except ValueError as e:
    print(str(e))
    Ku, Tu = None, None  

# Definição dos parâmetros PID de acordo com os métodos de Ziegler-Nichols
if Ku is not None:
    Kp_PID = 0.68 * Ku
    Ki_PID = Tu / 2
    Kd_PID = Tu * 0.125

    print(f"Parâmetros do Controlador PID: Kp={Kp_PID}, Ki={Ki_PID}, Kd={Kd_PID}")

    # Criar a função de transferência PID
    controller_PID = ct.TransferFunction([Kd_PID, Kp_PID, Ki_PID], [1])

    # Sistema com controle PID em malha fechada
    closed_loop_PID = ct.feedback(controller_PID * open_loop)

    # Simular a resposta ao degrau
    t = np.linspace(0, t_sim, 1000)
    _, y_PID = ct.step_response(closed_loop_PID, t)

    # Plotar a resposta do sistema
    plt.figure(figsize=(10, 6))
    plt.plot(t, y_PID, label="PID Control")
    plt.title('Resposta do Sistema com Controlador PID')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

    # Gráficos de Frequência (Bode)
    plt.figure(figsize=(10, 6))

    omega, mag_open, phase_open = ct.bode(open_loop, plot=False)
    omega, mag_closed_PID, phase_closed_PID = ct.bode(closed_loop_PID, plot=False)

    plt.semilogx(omega, 20 * np.log10(mag_open), label="Open Loop")
    plt.semilogx(omega, 20 * np.log10(mag_closed_PID), label="Closed PID Loop")
    plt.title('Gráficos Bode - Sistema em Malha Aberta e Controlador PID')
    plt.xlabel('Frequência (rad/s)')
    plt.ylabel('Magnitude (dB)')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()
else:
    print('Não foram encontrados os ganhos críticos adequados.')
