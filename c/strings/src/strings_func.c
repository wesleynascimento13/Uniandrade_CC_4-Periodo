#include <ctype.h>
#include <string.h>

#include "../lib/strings_func.h"
// Transforma a string em maiúsculas
void uppercase(char *str)
{
    for (int i = 0; str[i]; i++)
    {
        str[i] = toupper((unsigned char)str[i]);
    }
}

// Transforma a string em minúsculas
void lowercase(char *str)
{
    for (int i = 0; str[i]; i++)
    {
        str[i] = tolower((unsigned char)str[i]);
    }
}

// Remove espaços extras no início e final da string
void trimSpaces(char *str)
{
    char *inicio = str;
    while (isspace((unsigned char)*inicio))
        inicio++;

    char *fim = str + strlen(str) - 1;
    while (fim > inicio && isspace((unsigned char)*fim))
        fim--;

    memmove(str, inicio, fim - inicio + 1);
    str[fim - inicio + 1] = '\0'; // Finaliza a string
}

// Capitaliza as palavras na string
void capitalize(char *str)
{
    int capitalizeNext = 1;
    for (int i = 0; str[i]; i++)
    {
        if (isspace((unsigned char)str[i]))
        {
            capitalizeNext = 1;
        }
        else if (capitalizeNext)
        {
            str[i] = toupper((unsigned char)str[i]);
            capitalizeNext = 0;
        }
        else
        {
            str[i] = tolower((unsigned char)str[i]);
        }
    }
}