import java.util.Scanner;

/**
 * CodingBat groupSum question: http://codingbat.com/prob/p145416
 *
 * Question: Given an array of ints, is it possible to choose a
 * group of some of the ints, such that the group sums to the given target?
 *
 * Note: Modified to take sequence and target from standard input
 */
public class groupSum {

   public static void main(String[] args){
      Scanner scanner = new Scanner(System.in);
      String[] numsString = scanner.nextLine().split(" ");
      int target = Integer.parseInt(scanner.nextLine());

      int[] nums = new int[numsString.length];
      for(int index = 0; index < nums.length; index++){
         nums[index] = Integer.parseInt(numsString[index]);
      }


      System.out.println(groupSum(0, nums, target));
   }
   public static boolean groupSum(int index, int[] nums, int target) {
      //Base case
      if (index >= nums.length){
         return (target == 0)
      }

      //Current index being treated as a 1 and being removed
      if (groupSum(index + 1, nums, target - nums[index])){
         return true;
      }
      //Current index being treated as a 0, and NOT being removed
      if ((groupSum(index +1, nums, target))){
         return true;
      }
      //If both if conditions fail
      return false;
   }
}
