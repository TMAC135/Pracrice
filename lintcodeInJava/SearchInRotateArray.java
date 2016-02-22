/*
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array
*/

/*
Example
For [4, 5, 1, 2, 3] and target=1, return 2.

For [4, 5, 1, 2, 3] and target=0, return -1
*/


//刚开始的时候条件弄错了
public class Solution {
    /** 
     *@param A : an integer rotated sorted array
     *@param target :  an integer to be searched
     *return : an integer
     */
    public int search(int[] A, int target) 
    {
      if(A == null || A.length == 0) return -1;
      
      int start = 0;
      int end = A.length-1;
      int mid;
      
      while(start < end - 1)
      {
        mid = (start + end)/2;
        if(A[mid] == target) return mid;
        
        if(A[mid] >= A[start])
        {
        //这个条件是错的，并不是if条件句中并不是单一条件
        //   if(A[mid] < target) start = mid;
        //   else 
        //   {
        //       if(A[start] >= target) end=mid;
        //       else start = mid;
        //   }
            if(A[mid] >= target && A[start] <= target) end = mid;
            else start = mid;
        }else
        {
        //   if(A[mid] > target) end = mid;
        //   else 
        //   {
        //     if(A[end] <= target) end=mid;
            
        //     else start = mid;
        //   }
            if(A[mid] <= target && A[end] >= target) start = mid;
            else end = mid;
        }
        
      }
      //need to judge last time
      if(A[start] == target) return start;
      if(A[end] == target) return end;
      return -1;
    }
}

//同样的方法，但是最后不要判断start和end了
public class Solution 
{
    /** 
     *@param A : an integer rotated sorted array
     *@param target :  an integer to be searched
     *return : an integer
     */
    //上述二分法的解法不是很好，因为我们最后还单独判断了start和end是否相等
    //对于二分搜索法初试start和end条件不知道的情况下：
    //我们可以利用mid=(left+right)/2 的条件，每次我们都让left = mid +1 或者right=mid-1;这样我们的while条件就变成了
    //left<=right
    public int search(int[] A, int target) 
    {
      if(A == null || A.length == 0) return -1;
      
      int start = 0;
      int end = A.length-1;
      int mid;
      
      while(start <= end)
      {
        mid = (start+end)/2;
        if(A[mid] == target) return mid;
        
        if(A[mid] >= A[start])
        {
          if(A[mid] > target && A[start] <= target) end = mid - 1;
          else start = mid + 1;
        }else
        {
          if(A[mid] < target && A[end] >= target) start = mid + 1;
          else end = mid -1;
        }
      }
      return -1;
    }
}

//Follow up

/*
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array
*/

//经过实验，答案是肯定的，因为当有重复元素时，我们需要另行考虑
//例如输入是：[9,5,6,7,8,9,9,9,9,9,9], 8，如果按上述做法，返回就是false
//[9,5,5,5,5,5,6,9,9,9]



    public boolean search(int[] A, int target) 
    {
      if(A == null || A.length == 0) return false;
      
      int start = 0;
      int end = A.length-1;
      int mid;
      
      while(start <= end)
      {
        mid = (start+end)/2;
        if(A[mid] == target) return true;
        
        //相比较与版本1，这时候我们要单独考虑相等情况，即重复元素的影响，考虑问题要周全！！！！！！
        if(A[mid] > A[start])
        {
          if(A[mid] > target && A[start] <= target) end = mid - 1;
          else start = mid + 1;
        }else if(A[mid] < A[start])
        {
          if(A[mid] < target && A[end] >= target) start = mid + 1;
          else end = mid -1;
        }else //这时候A[mid] = A[start],说明遇到了重复元素
        {
        	start++;
        }
      }
      return false;

    }