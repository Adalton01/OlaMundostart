#include <stdio.h>
#include <stdlib.h>

int main() {
    char tamanho;

    // Solicita ao usuário que digite o tamanho desejado
    printf("Digite o Tamanho Desejado (P, G, M, N, X): ");
    scanf(" %c", &tamanho); // O espaço antes de %c descarta possíveis caracteres de espaço em branco

    // Verifica o valor digitado pelo usuário e exibe a mensagem correspondente
    if (tamanho == 'G' || tamanho == 'P') {
        printf("Sim, vamos para a quantidade.\n");
    }
    else if (tamanho == 'M' || tamanho == 'N') {
        printf("Desses só temos tamanho M.\n");
    }
    else if (tamanho == 'X' || tamanho == 'x') {
        printf("Este tamanho X temos 2 unidades.\n");
    }
    else {
        // Caso o valor seja inválido, exibe mensagem de erro e alerta sonoro
        printf("Digite somente G, P, M, N ou X.\a\n");
    }

    // Pausa o programa para que o usuário veja a mensagem antes do fechamento (Windows)
    system("pause");
    return 0;
}
