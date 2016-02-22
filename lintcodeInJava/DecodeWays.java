
/*
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
*/


// my solution, which is time exceed limit
public class Solution {
    public int numDecodings(String s) 
    {
    	if(s == null || s.length() == 0) return 0;

    	int index = 0 ;
        return helper(s, index);
    }

    //using recursion 
    private static int helper(String s, int index)
    {
    	//edge cases
    	if(index >= s.length()) return 0;
    	//make sure the next element of the index is not empty
    	if(index < s.length()-1)
    	{
    		int val = Integer.parseInt(s.substring(index,index+1));
    		if(val<=26) return 2 + helper(s,index+1) + helper(s,index+2);
    		else return 1 + helper(s,index+1) + helper(s,index+2);
    	}else 
    	{
    		return 1; // we reach the final element
    	}
    }
}

//Solution from others, Use DP
	public int numDecodings(String s) {  
        if (s.length()==0||s==null||s=="0") 
              return 0; 
  
          int[] dp = new int[s.length()+1];  
          dp[0] = 1;  
          
          if (isValid(s.substring(0,1)))
             dp[1] = 1;  
         else 
             dp[1] = 0; 
         
         for(int i=2; i<=s.length();i++){  
             if (isValid(s.substring(i-1,i)))  
                 dp[i] += dp[i-1];  
             if (isValid(s.substring(i-2,i)))  
                 dp[i] += dp[i-2];  
         }  
         return dp[s.length()];  
     }  
       
    public boolean isValid(String s){  
         if (s.charAt(0)=='0') 
             return false;  
         int code = Integer.parseInt(s);  
         return code>=1 && code<=26;  
     }
 }




