#include "stdio.h"

int main()
{
    int room_width, room_length, room_area;
    float cost_per_m2, room_cost;

    printf("\nEnter the width of the room (meters): ");
    scanf("%d", & room_width);
    
    printf("\nEnter the length of the room (meters): ");
    scanf("%d", & room_length);
    
    printf("\nEnter the cost of the carpet (per square meter): $");
    scanf("%f", & cost_per_m2);

    room_area = room_length * room_width;
    room_cost = room_area * cost_per_m2;

    printf("\nThe area of the room is: %dm", room_area);
    printf("The cost the carpet this room is: $%.2f\n", room_cost);

}