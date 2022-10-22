#include "stdio.h"

int main()
{
    float phone_card_price, tax_payable, total_price;
    const float tax=0.10;

    printf("\nEnter the phone card's price: $");
    scanf("%f", & phone_card_price);

    tax_payable = phone_card_price * tax;
    total_price = phone_card_price + tax_payable;

    printf("The cost of the phone card is: $%.2f\n", total_price);

}