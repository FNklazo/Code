// check age is below 2 or 12
// free if age <= 2, half if age <= 12, full price otherwise


#include <stdio.h>

int main()
{
    int age;
    float air_fare, ticket_cost;

    printf("Enter the air fare cost: $");
    scanf("%f", & air_fare);

    printf("Enter the age of the passenger: ");
    scanf("%d", & age);

    if (age <= 2)
        ticket_cost = 0;
    
    else if (age <= 12)
        ticket_cost = air_fare * 0.5;
        
    else 
        ticket_cost = air_fare;

    printf("Your ticket cost is: $%.2f", ticket_cost);

}