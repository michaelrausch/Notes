import java.util.Scanner;

/**
 * Author: Michael Cowie
 * Takes a string input from the user and prints all combinations of either a "+", "-" or empty
 * position in the place.
 * Originally done to complete the first half of a hackerrank question and practice recursion in java
 * and being unable to use uninitialized variables in parameters like python
 *
 Example input: "123"
 1+2+3
 1+2-3
 1+23
 1-2+3
 1-2-3
 1-23
 12+3
 12-3
 123
 */

public class plusMinusEmpty {

   public static void main(String args[]){
      Scanner userInput = new Scanner(System.in);
      String stringInput = userInput.nextLine();
      char[] charInput = stringInput.toCharArray();
      plusMinusEmpty(charInput);
   }

   private static void plusMinusEmpty(char[] userInput){
      int index = 0;
      String currentString = "";
      plusMinusEmptyRecursive(userInput, currentString, index);
   }


   private static void plusMinusEmptyRecursive(char[] userInput, String currentString, int index) {
      currentString += userInput[index];
      if (index == userInput.length - 1) {
         System.out.println(currentString);
         return;
      }
      String[] operators = {"+", "-", ""};
      for (String operator : operators) {
         plusMinusEmptyRecursive(userInput, currentString + operator, index + 1);
      }
   }
}
