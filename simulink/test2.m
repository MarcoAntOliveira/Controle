pkg load control

# Definir a função de transferência do sistema de segunda ordem
s = tf('s');
G = 1 / (s^2 + 3*s + 2);  # Sistema G(s) = 1 / (s^2 + 3s + 2)

# Definir o controlador PID
Kp = 350;  # Ganho proporcional
Ki = 300;  # Ganho integral
Kd = 50;   # Ganho derivativo

# Função de transferência do controlador PID
C = Kp + Ki/s + Kd*s;

# Sistema em malha fechada
T = feedback(C*G, 1);

# Simulação da resposta ao degrau
step(T);
title('Resposta ao Degrau de um Sistema Controlado por PID');
grid on;
pause(10);