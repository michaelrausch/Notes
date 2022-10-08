/*
    Self reminder code
*/

#include <stdio.h>


int main()
{
    float a = 5.25;
    int b = (int) a; //b = 5

    int x = 7, y = 5;
    float z;
    z = x / y; //z = 1 
    
    int x = 7, y = 5;
    float z;
    z = (float) x / y; // z = 1.4
    /*
        Note: z = (float) (x / y) evaluates to 1.000 because it does (x / y), then casts to a float
        The previous example is casting x to a float first, then doing float / int.
    */
    return 0;
}
