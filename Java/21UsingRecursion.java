import java.util.*;

/**
 * Takes a sequence of numbers from the user as input such as "1 9 11 5 6", and prints to combine
 * all combinations of the numbers that add to 21:
 * Example input: 1 9 11 5 6
 * Successfully outputs:
 * The values 1 9 11 Add up to 21
 * The values 1 9 5 6 Add up to 21
 */
public class TwentyOne {

   public static void main(String args[]){
      Scanner userInput = new Scanner(System.in);
      String stringInput = userInput.nextLine();

      //Takes string input to arrayList of integers to make it iterable, arrayList because unknown length
      ArrayList<Integer> allNum = new ArrayList<>();
      for (String num : stringInput.split(" ")){
         allNum.add(Integer.parseInt(num));
      }

      HashSet<ArrayList<Integer>> answer = twentyOne(allNum);

      if(answer.size() == 0){
         System.out.print("No possible number combinations equal 21");
         return;
      }
      //Iterating over each arrayList in the set to print to console
      for (ArrayList<Integer> solution : answer){
         System.out.print("The values ");
         for (Integer num : solution){
            System.out.print(num + " ");
         }
         System.out.println("Add up to 21");
      }
   }

   //Need to create this method because parameters cannot be initialized, then call recursion on other method.
   private static HashSet twentyOne(ArrayList<Integer> userInput){
      ArrayList<Integer> stack = new ArrayList<>();
      HashSet<ArrayList<Integer>> answer = new HashSet<>();
      return twentyOneRecursive(userInput, stack, answer);
   }

   private static HashSet<ArrayList<Integer>> twentyOneRecursive(ArrayList<Integer> userInput, ArrayList<Integer> stack, HashSet<ArrayList<Integer>> answer){
      //ListIterator is equivilent to enumerate in python
      ListIterator<Integer> userInputIterator = userInput.listIterator();
      while (userInputIterator.hasNext()){
         //Creating a new_stack object, since appending to the object updates in all recursive instances
         ArrayList<Integer> new_stack = new ArrayList<>(stack);
         new_stack.add(userInputIterator.next());

         int sum = sum(new_stack);
         if (sum == 21){
            answer.add(new_stack);
         } else if (sum < 21){
            twentyOneRecursive(new ArrayList<>(userInput.subList(userInputIterator.nextIndex(), userInput.size())), new_stack, answer);
         }
      }
      //Same HashSet in each recursive instance
      return answer;
   }

   //Method to calculate sum integers given an ArrayList of integers
   private static int sum(ArrayList<Integer> nums){
      int sum = 0;
      for (int num : nums){
         sum += num;
      }
      return sum;
   }
}
