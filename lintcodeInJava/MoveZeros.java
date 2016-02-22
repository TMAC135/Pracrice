
/*
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
*/

//双指针问题的一个总结：注意区分两个指针区分什么，这个是一般根据题目来确定的，确定了
//指针的范围之后，这是重点和难点

//这题比较巧妙，也没想出来，两个指针，首先我们的目的是将非零的数字按原顺序来输出
// 因此我们需要用一个指针来记录下一个非零的位置，另一个指针来遍历整个数组，当遇到0时，
//继续前进，当遇到非0数字时，我们与前一个指针的值交换

public class MoveZeros
{
	public static void main(String[] args) 
	{
		//test array [1,0,0,2,3,4]
		int[] array = {1,0,0,2,3,4};
		moveZeroes(array);
		for(int i:array)
		{
			System.out.print(i);
		}		
	}


	public static void moveZeroes(int[] nums) 
	{
		if(nums == null || nums.length == 0) return;

		// int j = 0;
		for(int i = 0 ,j =0; i < nums.length; i++)
		{
			if(nums[i] != 0) 
			{
				swap(nums,i,j++);
				// j++;
			}
		}
        
    }

    public static void swap(int[] nums, int i, int j)
    {
    	int tmp = nums[i];
    	nums[i] = nums[j];
    	nums[j] = tmp;
    }
}