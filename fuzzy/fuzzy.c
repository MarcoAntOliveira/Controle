#include <stdio.h>

// Funções de pertinência para variáveis de entrada
float pertinencia_baixo(float x) {
    if (x <= 20) return 1;
    if (x >= 30) return 0;
    return (30 - x) / 10.0;
}

float pertinencia_medio(float x) {
    if (x <= 20 || x >= 40) return 0;
    if (x <= 30) return (x - 20) / 10.0;
    return (40 - x) / 10.0;
}

float pertinencia_alto(float x) {
    if (x <= 30) return 0;
    if (x >= 40) return 1;
    return (x - 30) / 10.0;
}

// Definimos uma regra fuzzy simples
float regra_fuzzy(float temperatura, float umidade) {
    float temp_alto = pertinencia_alto(temperatura);
    float umid_baixo = pertinencia_baixo(umidade);
    
    // Se temperatura é ALTA E umidade é BAIXA, então saída é ALTO
    return temp_alto < umid_baixo ? temp_alto : umid_baixo;  // min(temp_alto, umid_baixo)
}

// Exemplo de defuzzificação simples
float defuzzificacao(float fuzzy_saida) {
    // Aqui, por simplicidade, multiplicamos o grau fuzzy por 100
    return fuzzy_saida * 100;
}

int main() {
    float temperatura = 35.0;
    float umidade = 15.0;

    float fuzzy_saida = regra_fuzzy(temperatura, umidade);
    float saida_crisp = defuzzificacao(fuzzy_saida);

    printf("Saída fuzzy: %.2f\n", fuzzy_saida);
    printf("Saída crisp (defuzzificada): %2f\n", saida_crisp);

    return 0;
}
