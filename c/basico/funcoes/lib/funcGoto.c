#include <stdio.h>
#include <stdlib.h>
#include "clear.h"

int main()
{
    int numero;
    
    printf("Digite um número: ");
    scanf("%d", &numero);

    if (numero < 0)
    {
        goto NEGATIVO;
    }
    else if (numero > 0)
    {
        goto POSITIVO;
    }
    else
    {
        goto ZERO;
    }

NEGATIVO:
 
    printf("O número [%d] é negativo.\n", numero);
    goto FIM;

POSITIVO:
   
    printf("O número [%d] é positivo.\n", numero);
    goto FIM;

ZERO:
   
    printf("Você inseriu o número ZERO.\n");
    goto FIM;

FIM:
printf("Fim do programa.\n");

}