pkg load control
s = tf('s');
G = 1 / (s^2 + 3*s + 2);  # Função de transferência de um sistema simples

# Simular a resposta ao degrau (step response)
step(G);
title('Resposta ao Degrau de um Sistema');
pause(10);