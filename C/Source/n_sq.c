#include "stdio.h"

int main()
{
    float n, n_sq;

    printf("\nEnter a number: ");
    scanf("%f", & n);

    n_sq = n * n;

    printf("Your number: %.0f", n);
    printf("Your number squared: %.0f\n", n_sq);

}