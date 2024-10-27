import numpy as np

# Coeficientes dos polinômios dos denominadores
den_G1 = [1, 2, 3, 4, 5]
den_G2 = [1, 5, 3, 1]
den_G3 = [1, 6, 3, 1, 1]
den_G4 = [1, 1, 0, 2]

# Calculando as raízes
raizes_G1 = np.roots(den_G1)
raizes_G2 = np.roots(den_G2)
raizes_G3 = np.roots(den_G3)
raizes_G4 = np.roots(den_G4)

# Exibindo os resultados
print("Raízes de G1(s):", raizes_G1)
print("Raízes de G2(s):", raizes_G2)
print("Raízes de G3(s):", raizes_G3)
print("Raízes de G4(s):", raizes_G4)
