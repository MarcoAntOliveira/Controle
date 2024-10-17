pkg load control

# Definir a função de transferência do sistema de primeira ordem
s = tf('s');
G = 1 / (s + 2);  # Sistema G(s) = 1 / (s + 2)

# Simulação da resposta ao impulso
figure;
impulse(G);
title('Resposta ao Impulso de um Sistema de Primeira Ordem');
grid on;

# Simular a resposta a uma entrada personalizada (sinal senoidal)
t = 0:0.01:10;  # Tempo de simulação
u = sin(t);     # Entrada senoidal

# Simulação da resposta com a entrada senoidal usando lsim
figure;
lsim(G, u, t);
title('Resposta a uma Entrada Senoidal');
xlabel('Tempo (s)');
ylabel('Saída do Sistema');
grid on;
pause(10);