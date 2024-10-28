pkg load control

# Definir a função de transferência de um sistema de segunda ordem
s = tf('s');
% % a)
% G = (s + 2) / (s^4 + 2*s^3 + 3*s^2 + 4*s+ 5 );  # Função de transferência mais complexa

%b)
G = (s^2 + 3*s + 2) / (s^3 + 5*s^2 + 3*s+ 1 );  # Função de transferência mais complexa

% % c)
% G = (s + 2) / (s^4 + 2*s^3 + 3*s^2 + 4*s+ 5 );  # Função de transferência mais complexa% 


% % d)
% G = (s + 2) / (s^4 + 2*s^3 + 3*s^2 + 4*s+ 5 );  # Função de transferência mais complexa


# Análise de Lugar das Raízes (Root Locus)
figure;
rlocus(G);
title('Lugar das Raízes de um Sistema de Segunda Ordem');
grid on;
pause(10)