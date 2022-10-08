#include <stdio.h>
/*Given a sequence of numbers, calculate a number which is higher than
 it's surrounding numbers (i.e the Magnitude) 
 
Example:
Input: 
1 7 20 20 25 300
27 25 2 0 5 2
100 100 100 0
4 5 5 0 100 -1
Output:
Number  Magnitude
   1        300
   2          5
   3        100
   4          5
*/
 
void peakPrint(int middleNum, int currentLine)
{
    printf("%4d", currentLine);
    printf("%11d\n", middleNum);
}
int main(void)
{
    printf("Number  Magnitude\n");
    int firstNum = 0;
    int middleNum = 0;
    int lastNum = 0;
    int currentLine = 1;
    scanf("%d %d", &firstNum, &middleNum);
    if(firstNum < 0 || middleNum < 0){
	return 0;
    }
    while(lastNum >= 0){
	scanf("%d", &lastNum);
	while(lastNum == middleNum){
            scanf("%d", &lastNum);
	}
	if(lastNum < 0){
	    return 0;
	}
	if(middleNum > firstNum && middleNum > lastNum){
            peakPrint(middleNum, currentLine);
	    currentLine += 1;
	}
	firstNum = middleNum;
	middleNum = lastNum;
    }
	
    return 0;
}
