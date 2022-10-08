/*
    Self reminder code
*/

#include <stdio.h>

void changeStringVal(char* input){
    input++; // Increase pointer by 1 type of bytes (i.e int = 4 memory addresses, char = 1 memory address)
    *(input + 1) += 5; // Derefernce pointer and increase value by 5
    printf("%s", input); //28
}

int main()
{
    char string[] = "123";
    changeStringVal(string);
    return 0;
}
