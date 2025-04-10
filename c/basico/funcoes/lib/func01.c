#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_STR 50

typedef struct
{
    char name[MAX_STR];
    float power;
    int lives;
    bool alive;

} Player;

float intToFloat(int n) {
    float resultado = (float)n;
    return resultado;
}

void halfConvert(int n){
    float num = intToFloat(n);
    float half = num * 0.5;
    printf("Metade: %.2f\n", half);
}

void menu(){
    printf("\n\n\n\n====Número Formatado===\n");
    int i = 100;
    printf("Número: %i\n", i);
    halfConvert(100);
    printf("\n=======================\n\n\n\n");
}

void imprimePlayer(Player *p){
    printf("====GAME OVER====\n");
    printf("Nome: %s\n", p->name);
    printf("Poder: %.4f\n", p->power);
    printf("Vidas: %d\n", p->lives);
    printf("Está vivo? %s\n", p->alive ? "Sim" : "Não");
    printf("===================\n");
}

int main(){
    Player players[] = {
        {.name = "Brunão", .power = 1500.0, .lives = 5, .alive = true},
        {.name = "Joãozão", .power = 3500.0, .lives = 50000, .alive = true},
        {.name = "Josevaldo", .power = 1500.0, .lives = 5, .alive = true}
    };

    for (int i = 0; i < 3; i++) {
        imprimePlayer(&players[i]);
    }

    menu();
    return 0;
}
