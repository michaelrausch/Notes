import java.util.HashMap;

/**
 * Returns nth fibonacci number with pruning added for efficiency
 */
public class fib {
   static HashMap<Integer, Integer> fibHash = new HashMap<>();

   public static void main(String[] args){
      fibHash.put(0,0);
      fibHash.put(1,1);
      System.out.println(fibonacci(12));
   }

   public static int fibonacci(int n) {
      int x = fibHash.containsKey(n - 1) ? fibHash.get(n - 1) : fibonacci(n - 1);
      fibHash.put(n - 1, x);
      int y = fibHash.containsKey(n - 2) ? fibHash.get(n - 2) : fibonacci(n - 2);
      fibHash.put(n - 2, y);
      return x + y;
   }
}
