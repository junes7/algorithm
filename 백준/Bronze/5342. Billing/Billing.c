#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct obj {
    char name[10];
    double pri;
};
int main(void) {
    double rlt = 0;
    char* st = (char*)malloc(sizeof(char) * 10);
    struct obj sup[7] = {
        {"Paper", 57.99},
        {"Printer", 120.50},
        {"Planners", 31.25},
        {"Binders", 22.50},
        {"Calendar", 10.95},
        {"Notebooks", 11.20},
        {"Ink", 66.95}};
    while (scanf("%s", st) != EOF) {
        for (int i = 0; i < 7; i++) {
            if (strcmp(sup[i].name, st) == 0) {
                rlt += sup[i].pri;
                break;
            }
        }
    }
    printf("$%.2lf", rlt);
    return 0;
}