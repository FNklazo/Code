// pollution index < 35 please, 35 >< 60 hazardous, >60 unpleasent

#include <stdio.h>

int main()
{
    char state_1 [10] = "Pleasant"; 
    char state_2 [10] = "Unpleasant";
    char state_3 [10] = "Hazardous"; 
    int pollution_index;
    

    printf("What is your city's pollution index?\nIndex: ");
    scanf("%d", & pollution_index);

    if (pollution_index <= 35)
        printf("Your city's pollution is: %s", state_1);
    
    else if (pollution_index <= 60)
        printf("Your city's pollution is: %s", state_2);
    
    else
        printf("Your city's pollution is: %s", state_3);
    

}