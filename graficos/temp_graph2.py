import matplotlib.pyplot as plt
import numpy as np

# Intervalo de zeta de 0.1 a 0.75
zeta = np.linspace(0.1, 0.75, 100)
# Função f(zeta)
f_zeta = np.log(0.02 * np.sqrt(1 - zeta**2))

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(zeta, f_zeta, label="f($\\zeta$) = $\\ln(0.02\\sqrt{1-\\zeta^2})$", color="blue")
plt.axhline(y=-4, color="red", linestyle="--", label="f($\\zeta$) ≈ -4")

# Adicionando títulos e legendas
plt.title("Aproximação de f($\\zeta$) para sistemas subamortecidos")
plt.xlabel("$\\zeta$")
plt.ylabel("f($\\zeta$)")
plt.legend()
plt.grid(True)

# Exibindo o gráfico
plt.show()
