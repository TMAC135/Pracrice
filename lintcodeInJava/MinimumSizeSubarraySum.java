/*
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint
*/

/*
Classifications:
1: subarray: did you mean it must be the extracted partially from the old array, or in other words, the subarray should be continiously from the old array
2: Can we use the util package to sort the solution first?
*/


import java.util.*;

public class Solution 
{
	// O(nlogn)，理解题目错误，因为子数组必须是连续的从原数组抽取
    public int minSubArrayLen(int s, int[] nums) {
        if(nums == null || nums.length == 0) return 0;
        //sort the array first 
       	int[] myNum = new int[nums.length];
       	System.arraycopy(nums,0,myNum,0,nums.length);
       	Arrays.sort(myNum);
       	//start from the end of the array then walk through the array in the back way
       	int sum=0;
       	for(int i=myNum.length-1;i>=0;i--)
       	{
       		sum += myNum[i];
       		if(sum >= s) return myNum.length - i;
       	}
       	return 0;
    }

    //O(nlogn)的解法，利用二分法
    public int minSubArrayLen(int s, int[] nums) 
    {

    }


}

//别人的解法：O(n)复杂度，抓住这题的重点，1:因为所有的元素都是正数，2:而且我们只能在一个子数组两边添加元素(子数组是连续的)
// 因此我们只需要我们首先找到包含第一个元素的最短子数组，即将end指针一直后移找到合适的位置，然后在根据初始的位置，移动
// end 或者 start 指针，知道end到达末尾. 
// 此题的精髓就是利用上述两个条件
public class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        if(nums==null || nums.length<1)
            return 0;

        int start=0, end=0, sum=0, min=Integer.MAX_VALUE;

        while(end<nums.length){
            sum+=nums[end];

            //optimize the array
            while(sum>=s){
                min=Math.min(min, end-start+1);
                sum-=nums[start++];
            }
            end++;
        }
        return min == Integer.MAX_VALUE ? 0 : min;
    }
}

//别人的解法，二分法，O(N*logN)复杂度
public class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        int i = 1, j = nums.length, min = 0;
        while (i <= j) {
            int mid = (i + j) / 2;
            if (windowExist(mid, nums, s)) {
                j = mid - 1;
                min = mid;
            } else i = mid + 1;
        }
        return min;
    }

    //次函数的目的是给定数组和制定window的size,能不能找到一个window的和大于s
    private boolean windowExist(int size, int[] nums, int s) {
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i >= size) sum -= nums[i - size];
            sum += nums[i];
            if (sum >= s) return true;
        }
        return false;
    }
}



//另一道十分类似的问题，maximum subarray：选出和最大的最大子数组和
//很好的思路（别人）：
/*
 1. 要么加入之前的数组加和之中（跟别人一组）

 2. 要么自己单立一个数组（自己单开一组）

 所以对于这个元素应该如何选择，就看他能对哪个组的贡献大。如果跟别人一组，能让总加和变大，还是跟别人一组好了；如果自己起个头一组，自己的值比之前加和的值还要大，那么还是自己单开一组好了。

所以利用一个sum数组，记录每一轮sum的最大值，sum[i]表示当前这个元素是跟之前数组加和一组还是自己单立一组好，然后维护一个全局最大值即位答案

sum[i] 包含i元素的子数组的和为最大的值，max是从0 ~ i中包含的子数组的最大值，注意区别
*/

//complexity(O(n))
public int maxSubArray(int[] A) {
         int[] sum = new int[A.length];
          
         int max = A[0];
         sum[0] = A[0];
  
         for (int i = 1; i < A.length; i++) {
             sum[i] = Math.max(A[i], sum[i - 1] + A[i]);
             max = Math.max(max, sum[i]);
         }
  
         return max;
     }

//如果我们要返回最大子数组的开始和结束index,things are getting a little complicated. 基本思路是差不多的，不过这时候我们要在每次比较的时候来更新索引了，
//同样是DP 的思想： start 和 end 表示全局的最大的索引，_start 表示包含当前元素(i)的最大子数组的开始位置，
//如果包含当前的最大值要比全局的大，我们更新start和end,否则我们就判断_start的关系

	public static int[] maxSubArray(int []nums)
	{
		int []res = new int[2];

		if(nums == null || nums.length == 0) return res;

		int max_so_far = Integer.MIN_VALUE;
		int max_end_here = nums[0];
		int start = 0;
		int end = 0;
		int _start = 0;

		for(int i=1;i < nums.length; i++)
		{
			//max_end_here = Math.max(max_end_here,max_end_here + nums[i]);
			// update the maximum subarray ending in index i
			if (nums[i] <= max_end_here + nums[i])
			{
				max_end_here = max_end_here + nums[i];
			}else
			{
				_start = i;
				max_end_here = nums[i];
			}
			// update the maximum subarray so far to index i
			if(max_so_far < max_end_here) 
			{
				max_so_far = max_end_here;
				start = _start;
				end = i;
			}
		}

		if(end == -1) // this is the case where all the element is the array are negative and decreasing
			{
				res[0] = start;
				res[1] = start;
			}else
			{
				res[0] = start;
				res[1] = end;
			}
		return res;
	}


/*
我的第二遍解法：O(n)解法，原理与上面是相同的
*/

public class Solution 
{
    /**
     * @param nums: an array of integers
     * @param s: an integer
     * @return: an integer representing the minimum size of subarray
     */
  
    /*
    1: the subarray should be continious from origibal array? 
    */
    //O(n) Solution
    public int minimumSize(int[] nums, int s) 
    {
      //boundary cases
      if(nums == null || nums.length == 0) return -1;
      
      int minLength = Integer.MAX_VALUE;
      int start = 0;
      int end = 0;
      int sum = 0;
      
      for(;end < nums.length; end++)
      {
        sum += nums[end]; 
        if(sum >= s)
        {
          int tmp = 0;
          while(sum >= s)
          {
            sum -= nums[start];
            start++;
          }
          minLength = Math.min(tmp,minLength);
        }
        
      }
      return minLength == Integer.MAX_VALUE ? -1 : minLength;
    }
}


