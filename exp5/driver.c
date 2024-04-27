#include "lib_mylib1.h"
#include "lib_mylib2.h"
#include <stdio.h>
void main()
{
    int ch, num1, num2;
start:
    printf("Enter 1 for GCD and 2 for LCM - ");
    scanf("%d", &ch);
    if (ch == 1 || ch == 2)
    {
        printf("Enter Num 1 - ");
        scanf("%d", &num1);
        printf("Enter Num 2 - ");
        scanf("%d", &num2);
        if (ch == 1)
        {
            gcd(ch, num1, num2);
        }
        if (ch == 2)
        {
            lcm(ch, num1, num2);
        }
    }
    else
    {
        printf("Enter correct choice \n");
        goto start;
    }
}