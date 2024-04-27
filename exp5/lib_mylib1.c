#include <stdio.h>
void gcd(int ch, int num1, int num2)
{
    int numerator, denominator, remainder, gcd, lcm;
    numerator = (num1 > num2) ? num1 : num2;
    denominator = (num1 < num2) ? num1 : num2;
    remainder = numerator % denominator;
    while (remainder != 0)
    {
        numerator = denominator;
        denominator = remainder;
        remainder = numerator % denominator;
    }
    gcd = denominator;
    printf("GCD of %d and %d = %d\n", num1, num2, gcd);
}
