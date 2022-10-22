#include <stdio.h>

int main()
{
    char client_name[30];
    float current_reading, prev_reading, total_reading;


    printf("What is your name?\n");
    fgets(client_name, 30, stdin);

    printf("What is your current reading?\n");
    scanf("%f", & current_reading);

    printf("What was your previous reading?\n");
    scanf("%f", & prev_reading);

    total_reading = current_reading - prev_reading;
    printf("Your final reading is $%.2f", total_reading);
    
    return 0;

}

