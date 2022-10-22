// write a program to determine if a number is odd or even
// request an integer to be entered then display the appropriate message

#include <stdio.h>

int main()
{
    int number;

    printf("Eneter an integer: ");
    scanf("%d", & number);

    if (number % 2)
        printf("%d is odd.", number);
    else
        printf("%d is even.", number);

}