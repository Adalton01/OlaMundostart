#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num;

    // Solicita ao usuário que digite o número da tabuada que deseja visualizar
    printf("\nDigite o número da tabuada que deseja ver: ");
    scanf("%d", &num);

    // Loop de 1 a 10 para calcular e mostrar a tabuada do número informado
    for (int i = 1; i <= 10; i++)
    {
        // Exibe a multiplicação no formato: i x num = resultado
        printf("%d x %d = %d\n", i, num, i * num);
    }

    // Pausa a execução para o usuário ver os resultados antes de fechar o programa (Windows)
    system("pause");

    return 0;
}
