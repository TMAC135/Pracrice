
/*
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
*/

/*
Given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
*/


//method 1: DFS, 注意edge case的边界条件以及recursion时候的参数问题
//注意此类问题要分析其中各地关系，因为要求是合法的括号表示，即每次右括号的总数不能超过左括号的总数！！！！
public class Solution {
    /**
     * @param n n pairs
     * @return All combinations of well-formed parentheses
     */
     
    //use dfs 
    public ArrayList<String> generateParenthesis(int n) {
        // Write your code here
        ArrayList<String> res = new ArrayList<String>();
        if (n <= 0) return res;
        
        dfs(n-1,n,"(",res);
        return res;
    }
    
    //dfs function, left and right means how many left and right parenthesis we need for the 
    //remaining string
    public void dfs(int left,int right,String tmp,ArrayList<String> res)
    {
        //boundary case
        if(left == 0 && right == 0) res.add(tmp);
        if(right < 0 || right < left) return;//very important, i don't deal with it at first
        
        if(left == 0)
        {
            dfs(0,right-1,tmp + ")",res);
        }else
        {
            dfs(left-1,right,tmp+"(",res);
            dfs(left,right-1,tmp+")",res);
        }
        
    }
}