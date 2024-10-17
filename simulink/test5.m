pkg load control

# Definir as matrizes de espaço de estados
A = [-2, -1; 1, 0];
B = [1; 0];
C = [1, 0];
D = 0;

# Criar o modelo no espaço de estados
sys = ss(A, B, C, D);

# Simulação da resposta ao degrau
figure;
step(sys);
title('Resposta ao Degrau de um Sistema no Espaço de Estados');
grid on;
pause(10);