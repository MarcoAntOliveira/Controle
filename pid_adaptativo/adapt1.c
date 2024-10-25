#include <stdio.h>

// Estrutura para armazenar os parâmetros PID e suas variáveis
typedef struct {
    float Kp, Ki, Kd;
    float integral;
    float erro_anterior;
} PIDController;

// Função para ajustar os ganhos PID adaptativamente
void ajuste_ganhos_pid(PIDController *pid, float erro, float delta_erro) {
    // Se o erro é alto, aumentamos Kp para uma resposta mais agressiva
    if (erro > 5) {
        pid->Kp = 2.0;
    } else if (erro > 2) {
        pid->Kp = 1.5;
    } else {
        pid->Kp = 1.0;
    }
    
    // Se a variação do erro é alta, aumentamos Kd para estabilidade
    if (delta_erro > 3) {
        pid->Kd = 1.0;
    } else {
        pid->Kd = 0.5;
    }

    // Se o erro é baixo mas persistente, aumentamos Ki para reduzir o erro residual
    if (erro < 1 && erro > -1) {
        pid->Ki = 0.5;
    } else {
        pid->Ki = 0.1;
    }
}

// Função PID com controle adaptativo
float pid_adaptativo(PIDController *pid, float setpoint, float temperatura_atual) {
    float erro = setpoint - temperatura_atual;
    float delta_erro = erro - pid->erro_anterior;

    // Ajuste dos ganhos PID
    ajuste_ganhos_pid(pid, erro, delta_erro);

    // Termo integral (acumulado ao longo do tempo)
    pid->integral += erro;

    // Termo derivativo (mudança na taxa de erro)
    float derivativo = delta_erro;

    // Saída do controlador PID
    float saida = (pid->Kp * erro) + (pid->Ki * pid->integral) + (pid->Kd * derivativo);

    // Atualiza o erro anterior
    pid->erro_anterior = erro;

    return saida;
}

int main() {
    // Parâmetros e variáveis do controlador
    PIDController pid = {1.0, 0.1, 0.5, 0.0, 0.0};
    float setpoint = 25.0;  // Temperatura desejada
    float temperatura_atual = 20.0;  // Temperatura inicial

    // Simulação do controle de temperatura
    for (int i = 0; i < 10; i++) {
        float controle = pid_adaptativo(&pid, setpoint, temperatura_atual);

        // Atualize a temperatura (exemplo simplificado)
        temperatura_atual += controle * 0.1;

        printf("Iteração %d: Controle = %.2f, Temperatura = %.2f, Kp = %.2f, Ki = %.2f, Kd = %.2f\n",
               i, controle, temperatura_atual, pid.Kp, pid.Ki, pid.Kd);
    }

    return 0;
}
