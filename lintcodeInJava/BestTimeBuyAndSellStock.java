

//版本1: 只能进行一次操作
public class Solution 
{
    /**
     * @param prices: Given an integer array
     * @return: Maximum profit
     */
  
/*
1:well, the brute force method, pass through the array as index of buy and find the max value 
for each given buy time, than we can maintain the global during the process we pass. - O(n^2) time complexity.
2:O(n) method, we pass through the array once, but at the same time, we keep the maxprofit and minvalue during
passing, since for each element, we have three options, it is buy time, sell time or nothing. 
*/
    public int maxProfit(int[] prices) 
    {
      //don't forget to add the special case
      if(prices == null || prices.length == 0) return 0;
      int maxProfit = Integer.MIN_VALUE;
      int min = Integer.MAX_VALUE;
      
      for(int i=0; i < prices.length; i++)
      {
        min = Math.min(min,prices[i]);
        maxProfit = Math.max(maxProfit,prices[i]-min);
      }
      return maxProfit;
    }
}

//版本2:可以进行多次操作，但是多次操作并不能重叠
class Solution 
{
    /**
     * @param prices: Given an integer array
     * @return: Maximum profit
     */
  
//we need to accumulate all possible profits of each transactions,thus
//we need a prev to store the buy time, then for each element
    public int maxProfit(int[] prices) 
    {
      if(prices == null || prices.length == 0) return 0;
      
      //第一遍的解法，错误的解法，开启新transaction 的条件错误了，并不是小于上一次开始买的时间,
      //而是小于当前交易的最大值。例如
      //[2,1,4,5,2,9,7] ==> 1-5 2-9,在判断2的时候，因为其比前以为小，则开启一个新的交易，而如果大的话，
      //则继续等待这次交易
      /*
      int prev = Integer.MAX_VALUE;
      int maxProfit;
      int curProfit = 0;
      
      for(int i=0;i<prices.length;i++)
      {
        if(prices[i] <= prev) //we start a new transaction
        {
          maxProfit += curProfit;
          prev = prices[i];
        }else
        {
          curProfit = Math.max(curProfit,prices[i] - prev);
        }
        
      }
      return maxProfit;
      */
    }
}

