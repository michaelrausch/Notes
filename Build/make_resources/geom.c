#include <stdio.h>
#include <math.h>

#include "gd.h"

// Calculate the distance to an x-y point.
int main() {
    double x = get_double("Enter the x valuee: ", -100, 100);
    double y = get_double("Enter the y value: ", -100, 100);

    double d = sqrt(pow(x, 2) + pow(y, 2));

    printf("Distance is %lf meters\n", d);
}
