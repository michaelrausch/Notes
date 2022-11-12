#include <stdio.h>

#include "gd.h"

int main(){
    double price, tip;
    printf("Enter price of meal: ");
    scanf("%lf", &price);

    printf("Enter tip amount (percent): ");
    scanf("%lf", &tip);

    double tipAmount = price * tip / 100.0;
    double total = price + tipAmount;
    printf("Tip amount: %lf\n", tipAmount);
    printf("Total amount: %lf\n", total);
}
