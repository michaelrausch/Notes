/**
 * Reverses a string using recursion
 */
public class ReverseString {

   public static void main(String[] args){
      System.out.println(reverseString("123"));
   }

   public static String reverseString(String input){
      if (input.length() == 1) {
         return input;
      } else{
         return input.charAt(input.length() - 1) + reverseString(input.substring(0, input.length() - 1));
      }
   }
}
