
/*
1: can I assume the array you give is always two dimension?
*/

//number of island
public class Solution 
{
    /**
     * @param grid a boolean 2D matrix
     * @return an integer
     */

     //we have another matrix to keep track of the element we have visit
     //这种方法不太好，因为我们没有必要创建多余的空间来记录是否被访问，取而代之的是
     //每次我们访问了1，我们用dfs和他相连的岛都链接在一起，而且将访问过的元素都置为0
    public int numIslands(boolean[][] grid) 
    {
    	if(grid == null || grid.length == 0) return 0;

    	int row = grid.length;
    	int column = grid[0].length;

    	int[][] status = new int[row][column];//0 represent this is not been visited

    	for(int i=0;i<row;i++)
    	{
    		for(int j=0;j<column;j++)
    		{
    			if (status[i][j] == 1) continue;
    			else
    			{

    			} 
    		}
    	}

    }

    public static boolean get(int row,int column,boolean[] grid)
    {
    	if(row)
    }

}


//向上述描述一样，我们用dfs加递归，
public class Solution {  
    private int m, n;   //可以将row,column设置为成员变量
      
    public int numIslands(char[][] grid) {  
        m = grid.length;  
        if (m == 0) return 0;  
        n = grid[0].length;  
        if (n == 0) return 0;  
          
        int ans = 0;  
        for (int i = 0; i < m; i++) {  
            for (int j = 0; j < n; j++) {  
                if (grid[i][j] != '1') continue;  
                  
                ans++;  
                dfs(grid, i, j);  
            }  
        }  
        return ans;  
    }  
      
      
    public void dfs(char[][] grid, int i, int j) {  
        if (i < 0 || i >= m || j < 0 || j >= n) return;  
          
        if (grid[i][j] == '1') {  
            grid[i][j] = '2';  
            dfs(grid, i - 1, j);  
            dfs(grid, i + 1, j);  
            dfs(grid, i, j - 1);  
            dfs(grid, i, j + 1);  
        }  
    }  
}



//我第二次写的

public class Solution 
{
    /**
     * @param grid a boolean 2D matrix
     * @return an integer
     */
  
  
    /*
    can we change the contend of the original array?
    bfs and dfs?
    */
    public int numIslands(boolean[][] grid) 
    {
      int res;
      if(grid == null || grid.length == 0) return 0;
      
      int row = grid.length;
      int col = grid[0].length;
      
      for(int i=0;i<row;i++)
      {
        
        for(int j=0;j<col;j++)
        {
          if(grid[i][j] == true)
          {
            res ++;
            dfs(grid,i,j);
          }
        }
        
      }
      return res;
    }
  
    public void dfs(boolean[][] grid,int row,int col)
    {
      if(row < 0 || row >= grid.length || col < 0 || col > grid[0].length) return;
      
      if(grid[row][col] == true)
      {
        grid[row][col] = false;
        dfs(grid,row-1,col);
        dfs(grid,row,col-1);
        dfs(grid,row+1,col);
        dfs(grid,row,col+1);
      }
    }
}


//如果我们不能修改原数组的内容，则我们需要另外创建一个二维矩阵来存储dfs相应位置是否被访问的flag,