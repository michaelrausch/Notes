import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Practicing recursion, using java.
 */
public class Odds {

   public static void main(String[] args){
      List<Integer> myList = new ArrayList<>(Arrays.asList(-3,1,2,3,4));
      for(int x : getOdds(myList)){
         System.out.print(x + " "); //-3 1 3
      }
   }

   /**
    * Given a list of integers, returns all odd numbers in the list.
    */
   public static List<Integer> getOdds(List<Integer> nums){
      return getOddsHelper(nums, new ArrayList<>(), 0);
   }

   /**
    * Recursive method for getOdds.
    * Private to hide implementation from user, now the client only needs to call getOdds with
    * no extra parameters
    */
   private static List<Integer> getOddsHelper(List<Integer> nums, ArrayList<Integer> result, Integer i){
      if (i == nums.size()){
         return result;
      }
      int num = nums.get(i) % 2;
      if (num < 0) num += 2; //-1 mod 2, is -1.

      if (num == 1){
         result.add(nums.get(i));
         return getOddsHelper(nums, result, i + 1);
      } else {
         return getOddsHelper(nums, result, i + 1);
      }
   }
}
