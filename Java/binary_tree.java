import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Simply, a binary tree.
 * Author: Michael Cowie
 */
public class Main {

   public static void main(String[] args){
      BinaryTree binaryTree = new BinaryTree();
      binaryTree.add(5);
      binaryTree.add(3);
      binaryTree.add(2);
      binaryTree.add(10);
      for(Integer nodeVal : binaryTree.bfsTraversal()){
         System.out.print(nodeVal + " "); //5 3 10 2
      }
   }

}

class Node {
   Integer value;
   Node left = null;
   Node right = null;
   public Node(int value){
      this.value = value;
   }
}

class BinaryTree {
   Node root;

   public BinaryTree(){
      this.root = null;
   }

   public void add(int value){
      if(this.root == null){
         this.root = new Node(value);
      } else{
         add_helper(this.root, value);
      }
   }

   public void add_helper(Node node, int value){
      //Check if traversing left
      if(value < node.value){
         //Check if leaf node
         if(node.left == null){
            node.left = new Node(value);
         } else{
            add_helper(node.left, value);
         }
         //Check if traversing right
      } else if(value > node.value){
         //Check if leaf node
         if(node.right == null){
            node.right = new Node(value);
         } else{
            add_helper(node.right, value);
         }
      }
   }

   public List<Integer> bfsTraversal(){
      List<Integer> traversalValue = new ArrayList<>();
      ArrayList<Node> queue = new ArrayList<>(Arrays.asList(this.root));
      while (queue.size() > 0){
         Node nodeToPop = queue.remove(0);
         if (nodeToPop != null) {
            traversalValue.add(nodeToPop.value);
            queue.add(nodeToPop.left);
            queue.add(nodeToPop.right);
         }
      }

      return traversalValue;
   }
}
