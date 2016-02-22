
/*
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
*/


//我的解法就是两遍遍历列表，第一次统计有多少0，1，2，然后第二次再复写数组中的元素
//follow up 没想出来，是利用三指针

/*
题解：

这道题就是运用指针来解决了，可以说叫3指针吧。

一个指针notred从左开始找，指向第一个不是0（红色）的位置；一个指针notblue从右开始往左找，指向第一个不是2（蓝色）的位置。

然后另一个新的指针i指向notred指向的位置，往后遍历，遍历到notred的位置。

这途中需要判断：

当i指向的位置等于0的时候，说明是红色，把他交换到notred指向的位置，然后notred++，i++。

当i指向的位置等于2的时候，说明是蓝色，把他交换到notblue指向的位置，然后notred--。

当i指向的位置等于1的时候，说明是白色，不需要交换，i++即可。
*/

public static void swap(int A[], int i, int j){
         int tmp = A[i];
         A[i]=A[j];
         A[j]=tmp;
	    }
    
     public static void sortColors(int A[]) {
         if(A == null || A.length==0)
             return;
             
         int notred=0;
         int notblue=A.length-1;
          
         while (notred<A.length&&A[notred]==0)
             notred++;
             
         while (notblue>=0&&A[notblue]==2)
             notblue--;
          
         int i=notred;
         while (i<=notblue){
             if (A[i]==0) {
                 swap(A,i,notred);
                 notred++;
                 i++;
             }else if (A[i]==2) {
                 swap(A,i,notblue);
                 notblue--;
             }else
                 i++;
         }
     }


//我的第二遍自己的做法
/*
注意如果题目要求并不是完全排序而是按照某规则分区域排序，可以利用类似快排的思想，利用指针将区域分为几个部分，
例如这题思想是用三个指针来区分三个区域，0～point0:红色，point0~point1:白色，point2~end:蓝色,
而point1~point2是我们需要遍历的元素
*/
class Solution {
    /**
     * @param nums: A list of integer which is 0, 1 or 2 
     * @return: nothing
     */
  
    //[1,0,1,2,0,1,1,0,2] 
    // 
    public void sortColors(int[] nums) 
    {
      if(nums == null || nums.length == 0) return;
      int point0 = 0;
      int point2 = nums.length-1;
      
      while(nums[point0] == 0) point0++;
      while(nums[point2] == 2) point2--;
      int point1 = point0;
      while(point1<=point2)
      {
        //three cases for the mid area
        if(nums[point1] == 0)
        {
          swap(nums,point0,point1);
          point0++;
          point1++;
        }else if(nums[point1] == 2)
        {
          swap(nums,point1,point2);
          point2--;
        }else point1++;
      }
    }
  
    public void swap(int[]nums,int index1,int index2)
    {
      if(index1 == index2) return;
      int tmp = nums[index1];
      nums[index1] = nums[index2];
      nums[index2] = tmp;
    }
}

/*
类似facebook的面试题：
Given a input of integers: {10, 555, 100000, 100, 9}

Given a categorizer function: enum cat(int input) = S, M, L

Output: {10, 9, 555, 100, 100000}

example of cat: < 100 S; else < 1000 M; else L


给1个数组，并根据给出的cat function将数组按小中大的范围重新排序后输出（S , M , L）， 不要求相对范围内的顺序。

*/
//解法根上述一样



