#include<stdio.h>
int main() {
    for (int i=1;i<=5;i++) {
        for (int j=1; j<=5-i; j++){
            printf(" ");
        }
        for (int k=1; k <= i*2-1; k++) {
            printf("*");
        }
        print('\n');
    }
    return 0;
}