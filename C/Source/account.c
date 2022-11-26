#include "stdio.h"

int main()
{
    int acc_num;
    float bal, new_bal, month_total, cred_limit, cred_total;

    while (acc_num != -1)
        {
            printf("\nPlease enter the account number: ");
            scanf("%d", & acc_num);

            printf("\nEnter the account balance from the month's beginning: $");
            scanf("%f", & bal);
            
            printf("\nEnter the total of this month's purchases: $");
            scanf("%f", & month_total);

            printf("\nEnter the total of this month's credits spent: $");
            scanf("%f", & cred_total);
        
            printf("\nEnter the customer's credit limit for this month: $");
            scanf("%f", & cred_limit);
        
            new_bal = bal - (cred_total - cred_limit);

            if (cred_total > cred_limit)
                {
                    printf("\nCredit Exceeded.");
                    printf("\nAccount number: %d" "\nCredit Limit: $%.2f" "\nCredit Total: $%.2f" "\nNew Balance: $%.2f\n", 
                    acc_num, cred_limit, cred_total, new_bal);
                }
        }
}