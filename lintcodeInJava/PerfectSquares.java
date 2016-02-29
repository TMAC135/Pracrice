


/*
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
*/


//我的第一遍解发，想用dfs解，但是不对,
public class Solution 
{
    public int numSquares(int n) 
    {
      int res;
      res = helper(n,n,0);
      return res == -1?0:res;
    }
  
  
    //use dfs 
    public int helper(int target, int num, int count)
    {
      //edge case
      if(num <= 0 || target<= 0) return -1;
      
      if(isValid(num) == true) return count+1;
      else
      {
        //we are trying to find the largest perfect square number
        while(num >= 1)
        {
          int min=Integer.MAX_VALUE;
          if(isValid(num--) == true)
          {
            int tmp = helper(target - num,target- num,count+1);
            if(tmp != -1) min = Math.min(min,tmp);
          }
          return min; 
        }
      }
    }
  
    //function to judge if the num is a perfect number
    public boolean isValid(int num)
    {
      if(num <= 0) return false;
      int tmp = (int)Math.sqrt(num);
      return tmp*tmp==num?true:false;
    }
}

//别人的第一种解发，用递归解,即使通过了oj,但是时间复杂度还是O(n),递归要从2开始，然后用用一个全局变量min来保存最小值
public class Solution 
{
    public int numSquares(int n) 
    {
    	if(n <= 0) return 0;
    	int res=n;
    	int num = 2;
    	while(num*num <= n)
    	{
    		int a = n/(num*num);
    		int b = n%(num*num);
    		res = Math.min(res,a+numSquares(b));
    		num++;
    	}
    return res;
    }
}

//别人的第二种解乏，用dp解,
/*
我们建立一个长度为n+1的一维dp数组，将第一个值初始化为0，其余值都初始化为INT_MAX, i从0循环到n，
j从1循环到i+j*j <= n的位置，然后每次更新dp[i+j*j]的值，动态更新dp数组，其中dp[i]表示正整数i
能少能由多个完全平方数组成，那么我们求n，就是返回dp[n]即可，也就是dp数组的最后一个数字，参见代码如下：
*/

public class Solution
{
	public int numSquares(int n)
	{
		if(n <= 0) return 0;
		int[] dp = new int[n + 1];
		Arrays.fill(dp,Integer.MAX_VALUE);//如何用特定值来初始化数组
		dp[0] = 0;
		for(int i=0;i<=n;i++)
		{
			for(int j=1;i+j*j<=n;j++)
			{
				dp[i+j*j] = Math.min(dp[i+j*j],dp[i]+1);
			}
		}
		return dp[dp.length - 1];
	}
}

//别人的第三种解乏，更巧妙
/*
先来看第一种很高效的方法，根据四平方和定理，任意一个正整数均可表示为4个整数的平方和，其实是可以表示为4个以内的平方数之和，
那么就是说返回结果只有1,2,3或4其中的一个，首先我们将数字化简一下，由于一个数如果含有因子4，那么我们可以把4都去掉，并不影响结果，
比如2和8,3和12等等，返回的结果都相同，读者可自行举更多的栗子。还有一个可以化简的地方就是，如果一个数除以8余7的话，那么肯定是由4个完全平方数组成，
这里就不证明了，因为我也不会证明，读者可自行举例验证。那么做完两步后，一个很大的数有可能就会变得很小了，大大减少了运算时间，下面我们就来尝试的将其拆为两个平方数之和，
如果拆成功了那么就会返回1或2，因为其中一个平方数可能为0. 
*/
