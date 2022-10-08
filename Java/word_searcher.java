/**
 * Given a maze, represented by a list of strings.
 * Returns the occurrences of a specified word count.
 * Note: Must be square grid
 *
 * Count specification:
 * Left,Up,Down,Right. For each step, it does not look in all directions again. Word must be continuous.
 */
public class MazeWordFinder {

   public static void main(String[] args){
      String[] myList = {
         "XTXX",
         "TEST",
         "MSPP",
         "HTHI"
      };
      String searchWord = "TEST";
      System.out.println(countWordOccurence(myList, searchWord)); //2
   }


   private static int countWordOccurence(String[] userInput, String searchWord){
      char[][] grid = convertTo2DArray(userInput);
      int occurences = 0;
      for(int row = 0; row < grid.length; row ++){
         for(int col = 0; col < grid[0].length; col ++){
            if(grid[row][col] == searchWord.charAt(0)){
               occurences += countWordOccurrenceHelper(row, col, grid, searchWord);
            }
         }
      }
      return occurences;
   }

   private static int countWordOccurrenceHelper(int row, int col, char[][] grid, String searchWord){
      int[] dRow = {-1, 0, 1, 0}; //N, E, S, W
      int[] dCol = {0, 1, 0, -1}; //N, E, S, W

      int occurrences = 0;
      //dir used to change all four directions
      for(int dir = 0; dir < 4; dir++){
         int cur_row = row;
         int cur_col = col;
         for(int move = 0; move < searchWord.length(); move++){

            //Test for invalid position or incorrect letter
            if(cur_row < 0 || cur_row >= grid.length ||
               cur_col < 0 || cur_col >= grid[0].length ||
               !(grid[cur_row][cur_col] == searchWord.charAt(move))){
               break;
            //
            } else if (move == searchWord.length() - 1){
               occurrences += 1;
            }
            cur_row += dRow[dir];
            cur_col += dCol[dir];
         }
      }
      return occurrences;
   }

   private static char[][] convertTo2DArray(String[] stringGrid){
      char[][] twoDGrid = new char[stringGrid.length][stringGrid[0].length()];
      for(int row = 0; row < stringGrid.length; row++){
         for(int col = 0; col < stringGrid[0].length(); col++){
            twoDGrid[row][col] = stringGrid[row].charAt(col);
         }
      }
      return twoDGrid;
   }
}
