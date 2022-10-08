/*Reads from standard input until EOF and displays the count of each character
Accepts non alphabetical characters but simply skips over them

Example:
Input:
aBbcCcDDDDeeeeefFfFfFG
Output:
A: 1
B: 2
C: 3
D: 4
E: 5
F: 6
G: 1
Also prints letters which include 0, but are not shown in this docstring
*/

#include <stdio.h>
#include <ctype.h>

int main(void)

{
    int array[26] = {0};
    char c = getchar();
    while(c != EOF){
	if(isalpha(c)){
		c = toupper(c);
		array[c-65] = array[c-65] + 1;
	}
	c = getchar();
    }
    for(int x = 0; x <= 25; x++){
	printf("%c: %d\n", x + 65, array[x]);
    }
}
