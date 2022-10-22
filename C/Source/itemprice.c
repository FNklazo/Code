#include "stdio.h"

int main()
{
    float price, new_price;
    const float discount = 0.12;

    printf("\nEnter the item's price: $");
    scanf("%f", & price);

    new_price = price - ( price * discount);

    printf("Your discounted price is: $%.2f\n", new_price);

}