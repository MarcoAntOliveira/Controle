# Controle
Respositorio destinado aos codigos gerados para disciplina de sistemas de controle


# Resumo de Fórmulas de Sistemas de Controle

## 1. Função de Transferência

**Fórmula:**
$$
G(s) = \frac{Y(s)}{U(s)}
$$

**Finalidade:**
Relaciona a saída \( Y(s) \) com a entrada \( U(s) \) no domínio de Laplace. Útil para analisar sistemas LTI.

---

## 2. Transformada de Laplace

**Fórmula:**
$$
\mathcal{L}\{f(t)\} = \int_0^{\infty} f(t) e^{-st} dt
$$

**Finalidade:**
Transforma equações diferenciais em algébricas no domínio \( s \).

---

## 3. Equação Característica

**Fórmula:**
$$
a_0 s^n + a_1 s^{n-1} + \dots + a_n = 0
$$

**Finalidade:**
Determina os pólos do sistema, que afetam a estabilidade e a resposta temporal.

---

## 4. Lugar das Raízes

**Equação:**
$$
1 + G(s)H(s) = 0
$$

**Finalidade:**
Mostra como os pólos variam com o ganho \( K \). Ferramenta útil de projeto.

---

## 5. Critério de Routh-Hurwitz

**Condição de Estabilidade:**
Todos os elementos da 1ª coluna da tabela de Routh devem ser positivos.

**Finalidade:**
Verifica estabilidade sem precisar calcular raízes.

---

## 6. Erro em Regime Permanente

Para sistemas com realimentação unitária:

- Constantes de erro:
  $$
  K_p = \lim_{s \to 0} G(s), \quad
  K_v = \lim_{s \to 0} sG(s), \quad
  K_a = \lim_{s \to 0} s^2 G(s)
  $$

- Erros:
  - Degrau (Tipo 0): \( E_{ss} = \frac{1}{1 + K_p} \)
  - Rampa (Tipo 1): \( E_{ss} = \frac{1}{K_v} \)
  - Parábola (Tipo 2): \( E_{ss} = \frac{1}{K_a} \)

**Finalidade:**
Avalia a precisão do sistema com diferentes tipos de entrada.

---

## 7. Requisitos de Desempenho (Resposta ao Degrau)

### Sistema de 2ª ordem:

**Função de Transferência:**
$$
G(s) = \frac{\omega_n^2}{s^2 + 2\zeta \omega_n s + \omega_n^2}
$$

- \( \omega_n \): frequência natural
- \( \zeta \): fator de amortecimento

---

### a) Tempo de Subida \( t_r \)

$$
t_r \approx \frac{1.8 \text{ a } 2.2}{\omega_n}
$$

---

### b) Tempo de Pico \( t_p \)

$$
t_p = \frac{\pi}{\omega_n \sqrt{1 - \zeta^2}}
$$

---

### c) Sobressinal Máximo \( M_p \)

$$
M_p = e^{\left(-\frac{\pi \zeta}{\sqrt{1 - \zeta^2}}\right)} \times 100\%
$$

---

### d) Tempo de Acomodação \( t_s \)

- Para 2%:
  $$
  t_s \approx \frac{4}{\zeta \omega_n}
  $$
- Para 5%:
  $$
  t_s \approx \frac{3}{\zeta \omega_n}
  $$

---

### e Fator de Amortecimento   $\zeta$

- $ \zeta = 0 $ : sistema oscilatório puro
- $ 0 < \zeta < 1 $ : subamortecido
- $ \zeta = 1 $ : criticamente amortecido
- $ \zeta > 1 $ : superamortecido

---

## 8. Controlador PID

**Fórmula no domínio de Laplace:**
$$
U(s) = K_p + \frac{K_i}{s} + K_d s
$$

**Finalidade:**
Melhora desempenho do sistema corrigindo erro com ação proporcional, integral e derivativa.

---
