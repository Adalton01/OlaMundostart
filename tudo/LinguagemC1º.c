#include <stdio.h>
#include <stdlib.h>
main()
{
    char tamanho;
    printf("Digite o Tamanho Desejado P ou G : ");
    scanf("%c", &tamanho);
    if (tamanho == 'G' || tamanho =='P')
        printf("Sim Vamos Para Quantidade \n");
    else if ( tamanho == 'M' || tamanho == 'N')
        printf("Desse so temos Tamanho M \n");
    else if (tamanho =='x' || tamanho == 'X')
        printf("Este tamanho X Temos 2 Unid  \n");
    else
        printf("Digite Somente G,P,M,N . \a");

    system("pause");
}







