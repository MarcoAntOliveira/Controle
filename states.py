import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

class StateSpaceModel:
    def __init__(self, A, B, C, D):
        self.A = np.array(A)
        self.B = np.array(B)
        self.C = np.array(C)
        self.D = np.array(D)

    def dynamics(self, t, x, u_func):
        # Definir a entrada como uma função do tempo
        u = u_func(t)
        # Dinâmica do sistema: dx/dt = Ax + Bu
        dxdt = self.A @ x + self.B @ u
        return dxdt

    def output(self, x, u):
        # Calcular a saída: y = Cx + Du
        y = self.C @ x + self.D @ u
        return y

    def simulate(self, x0, u_func, t_span, t_eval):
        # Simula a resposta do sistema ao longo do tempo
        sol = solve_ivp(
            fun=lambda t, x: self.dynamics(t, x, u_func),
            t_span=t_span,
            y0=x0,
            t_eval=t_eval
        )
        # Calcular a saída para cada ponto no tempo
        y = np.array([self.output(x, u_func(t)) for t, x in zip(sol.t, sol.y.T)])
        return sol.t, sol.y.T, y

# Exemplo de uso
A = [[0, 1], [-2, -3]]  # Matriz A
B = [[0], [1]]          # Matriz B
C = [[1, 0]]            # Matriz C
D = [[0]]               # Matriz D

# Definir função de entrada como uma função do tempo (exemplo: entrada constante u(t) = 1)
u_func = lambda t: np.array([1])

# Parâmetros iniciais e tempo de simulação
x0 = [0, 0]             # Estado inicial
t_span = (0, 10)        # Intervalo de tempo
t_eval = np.linspace(0, 10, 100)  # Pontos de avaliação para o tempo

# Criar o modelo e simular
model = StateSpaceModel(A, B, C, D)
t, x, y = model.simulate(x0, u_func, t_span, t_eval)

# Plotar os resultados
plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title("Resposta do Estado x(t)")
plt.xlabel("Tempo")
plt.ylabel("Estado")
plt.legend(['x1', 'x2'])

plt.subplot(2, 1, 2)
plt.plot(t, y)
plt.title("Saída y(t)")
plt.xlabel("Tempo")
plt.ylabel("Saída y")

plt.tight_layout()
plt.show()
    