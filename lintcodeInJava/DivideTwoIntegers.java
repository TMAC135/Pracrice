public class Solution 
{
    /**
     * @param dividend the dividend
     * @param divisor the divisor
     * @return the result
     */
  
  /*
  1: can we use add operation?
  */
  
    //第一次解法，没有考虑全overcase的解法，因为 int 的范围是(-2^31 ~ 2^31-1),
  //当被除数是－2^31和除数是+-1时候，我们应该另行考虑
  //另外修改后的解法虽然是对的，但O(n)的复杂度超过了时间限度
    public int divide(int dividend, int divisor) 
    {
      //overflow case
      if(divisor == 0 ) return Integer.MAX_VALUE;
      if(dividend == Integer.MIN_VALUE)
      {
          if(divisor == 1) return Integer.MIN_VALUE;
          if(divisor == -1) return Integer.MAX_VALUE;
      }
      
      //transfer all the operation to positive number manipulation
      int res = 0;
      int remain = Math.abs(dividend);
      int absDivisor = Math.abs(divisor);
      
      while(remain >= absDivisor)
      {
        remain -= absDivisor;
        res++;
      }
      
      if((divisor < 0 && dividend < 0) || (divisor > 0 && dividend > 0) ) return res;
      else return -res;
      

    }

    //第二次解法，类似于二分法，并不是减去一定值，而是与上次的结果比较
    //但是结果仍然超时
	public int divide(int dividend, int divisor) 
    {
      //overflow case
      if(divisor == 0 ) return Integer.MAX_VALUE;
      if(divisor == 1) return dividend;
      if(divisor == -1)
      {
          if(dividend == Integer.MIN_VALUE) return Integer.MAX_VALUE;
          else return -dividend;
      }

      //use binary method for more efficient solution 
      int res = 0;
      int remain = Math.abs(dividend);
      int absDivisor = Math.abs(divisor);
      
      while(remain >= absDivisor)
      {
        int pow = 1;
        int sum = absDivisor;
        while(sum + sum < remain)
        {
          sum += sum;
          pow += pow;
        }
        remain -= sum;
        res += pow;
      }
      
      if((divisor < 0 && dividend < 0) || (divisor > 0 && dividend > 0) ) return res;
      else return -res;
  
    }

    //第三种解法，别人的解法
    /*
	这道题属于数值处理的题目，对于整数处理的问题，在Reverse Integer中我有提到过，比较重要的注意点在于符号和处理越界的问题。
	对于这道题目，因为不能用乘除法和取余运算，我们只能使用位运算和加减法。比较直接的方法是用被除数一直减去除数，直到为0。
	这种方法的迭代次数是结果的大小，即比如结果为n，算法复杂度是O(n)。

	那么有没有办法优化呢？ 这个我们就得使用位运算。我们知道任何一个整数可以表示成以2的幂为底的一组基的线性组合，
	即num=a_0*2^0+a_1*2^1+a_2*2^2+...+a_n*2^n。基于以上这个公式以及左移一位相当于乘以2，我们先让除数左移直到大于被除数之前得到一个最大的基。
	然后接下来我们每次尝试减去这个基，如果可以则结果增加加2^k,然后基继续右移迭代，直到基为0为止。
	因为这个方法的迭代次数是按2的幂直到超过结果，所以时间复杂度为O(logn)。代码如下
    */

	//这种数值处理的题目在面试中还是比较常见的，类似的题目有Sqrt(x)，Pow(x, n)等。上述方法在其他整数处理的题目中也可以用到，大家尽量熟悉实现这些问题。
    public int divide(int dividend, int divisor) {  
	    if(divisor == 0)  
	    {  
	        return Integer.MAX_VALUE;  
	    }  
	    boolean isNeg = (dividend^divisor)>>>31 == 1;  
	    int res = 0;  
	    if(dividend == Integer.MIN_VALUE)  
	    {  
	        dividend += Math.abs(divisor);  
	        if(divisor == -1)  
	        {  
	            return Integer.MAX_VALUE;  
	        }  
	        res++;  
	    }  
	    if(divisor == Integer.MIN_VALUE)  
	    {  
	        return res;  
	    }  
	    dividend = Math.abs(dividend);  
	    divisor = Math.abs(divisor);  
	    int digit = 0;  
	    while(divisor <= (dividend>>1))  //why????
	    {  
	        divisor <<= 1;  
	        digit++;  
	    }  
	    while(digit>=0)  
	    {  
	        if(dividend>=divisor)  
	        {  
	            res += 1<<digit;  
	            dividend -= divisor;  
	        }  
	        divisor >>= 1;  
	        digit--;  
	    }  
	    return isNeg?-res:res;  
    }
}


www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=125284&fromuid=109727