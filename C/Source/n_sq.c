#include "stdio.h"

int main()
{
    float n, n_sq;

    printf("\nEnter a number: ");
    scanf("%f", & n);

    n_sq = n * n;

    printf("\nYour number: %.0f", n);
    printf("\nYour number squared: %.0f\n", n_sq);

}