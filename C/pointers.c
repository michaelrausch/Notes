/*
    Self reminder code
*/

#include <stdio.h>

void pointerFunc(int* iptr){
    /* Print the value pointed to by iptr */
    printf("value %d\n", *iptr);
    
    /* 
       Print the address pointed to by iptr.
       By previously specifying that it is an int
       pointer, we now know the value will be at
       this address + 32 bits of range.
    */
    
    printf("located at memory address %p\n", iptr);
    
    /* Print the address of iptr */
    printf("with the pointer located at %p", &iptr);
}

int main(){
        
    int i = 1337;
    int* foo = &i;
    pointerFunc(foo);
    return 0;
}

