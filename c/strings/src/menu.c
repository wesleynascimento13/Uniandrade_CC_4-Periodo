#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include "../lib/menu.h"
#include "../lib/strings_func.h"
#include <limits.h>
#include <float.h>

#define MAX_STRING CHAR_MAX // Tamanho máximo da string baseado em CHAR_MAX

void showMenu()
{
    printf("Dentro menu...\n");
    char input[MAX_STRING + 1] = {0}; // String manipulada pelo usuário
    bool rodando = true;              // Controle do loop principal

    while (rodando)
    {
        printf("\n--- Menu ---\n");
        printf("1. Inserir uma string\n");
        printf("2. Transformar em maiúsculas (uppercase)\n");
        printf("3. Transformar em minúsculas (lowercase)\n");
        printf("4. Remover espaços extras (trim)\n");
        printf("5. Capitalizar palavras\n");
        printf("6. Exibir limites da linguagem C\n");
        printf("7. Sair\n");
        printf("Escolha uma opção: ");

        int opcao;
        if (scanf("%d", &opcao) != 1)
        { // Evita entrada inválida
            printf("Entrada inválida! Por favor, tente novamente.\n");
            while (getchar() != '\n')
                ; // Limpa o buffer
            continue;
        }
        getchar(); // Limpa o buffer após o número

        switch (opcao)
        {
        case 1:
            printf("Digite sua string (máx. %d caracteres): ", MAX_STRING);
            fgets(input, sizeof(input), stdin);
            input[strcspn(input, "\n")] = '\0'; // Remove o \n
            break;
        case 2:
            uppercase(input);
            printf("Resultado: %s\n", input);
            break;
        case 3:
            lowercase(input);
            printf("Resultado: %s\n", input);
            break;
        case 4:
            trimSpaces(input);
            printf("Resultado: %s\n", input);
            break;
        case 5:
            capitalize(input);
            printf("Resultado: %s\n", input);
            break;
        case 6:
            exibirLimites();
            break;
        case 7:
            printf("Encerrando o programa.\n");
            rodando = false; // Encerra o loop
            break;
        default:
            printf("Opção inválida! Tente novamente.\n");
        }
    }
}

void exibirLimites()
{
    printf("\n--- Limites Inteiros ---\n");
    printf("INT_MAX: %d\n", INT_MAX);
    printf("INT_MIN: %d\n", INT_MIN);
    printf("CHAR_MAX: %d\n", CHAR_MAX);
    printf("CHAR_MIN: %d\n", CHAR_MIN);

    printf("\n--- Limites de Ponto Flutuante ---\n");
    printf("FLT_MAX: %e\n", FLT_MAX);
    printf("FLT_MIN: %e\n", FLT_MIN);
    printf("DBL_MAX: %e\n", DBL_MAX);
    printf("DBL_MIN: %e\n", DBL_MIN);
}