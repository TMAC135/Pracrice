


/*
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
*/

/*
example:
Given board =

[
  "ABCE",
  "SFCS",
  "ADEE"
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false
*/

//我的第一次解法，利用递归，即dfs,这题的难点是如果控制状态矩阵-visited[][]
//另一个难点就是如何确立edge case ->       if (start >= word.length()) return true;
      // if(row < 0 || row >= board.length || col < 0 || col >= board[0].length) return false;
public class Solution 
{
    /**
     * @param board: A list of lists of character
     * @param word: A string
     * @return: A boolean
     */
    public boolean exist(char[][] board, String word) 
    {
      //special case
      if(board == null || board.length == 0 || word == null
          ||word.length() == 0) return false;
      int row = board.length;
      int col = board[0].length;
      if(word.length() > row*col) return false;
      
      boolean[][] visited = new boolean[row][col];
      for(int i = 0; i < row; i++)
      {
        
        for(int j = 0; j < col; j++)
        {
          if(helper(board,i,j,visited,word,0) == true) return true;
          else visited = new boolean[row][col];
                   
        }
      }
      return false;
      
    }
  
    //helper funtion to determine whether there is word in the specific position in the board
    public boolean helper(char[][] board, int row,int col,boolean[][] visited,String word,int start)
    {
      //edge case
      if (start >= word.length()) return true;
      if(row < 0 || row >= board.length || col < 0 || col >= board[0].length) return false;
      
      if(visited[row][col] == false && word.charAt(start) == board[row][col])
      {
        visited[row][col] = true;
        boolean flag = helper(board,row-1,col,visited,word,start+1) 
          || helper(board,row,col-1,visited,word,start+1)
              || helper(board,row+1,col,visited,word,start+1) 
          || helper(board,row,col+1,visited,word,start+1);
        //if we haven't find the word, we need to set the visited to false again
        if(flag == false) visited[row][col] = false;
        return flag;
      }else return false;
      
    }
}