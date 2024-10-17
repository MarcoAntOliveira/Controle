pkg load control

# Definir a função de transferência de um sistema de segunda ordem
s = tf('s');
G = (s + 3) / (s^3 + 5*s^2 + 6*s + 4);  # Função de transferência mais complexa

# Análise de Lugar das Raízes (Root Locus)
figure;
rlocus(G);
title('Lugar das Raízes de um Sistema de Segunda Ordem');
grid on;
pause(10)