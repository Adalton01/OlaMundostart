#include <stdio.h>
#include <stdlib.h>

main()
{
  int num;
  printf("\n Digite a Tabuada \n");
  scanf("%d", &num);

  for (int i = 1; i <= 10; i++)
    printf(" \n %d x %d = %d \n", i, num, i * num);

  system("pause");
}
