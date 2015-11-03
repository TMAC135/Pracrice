"""
Given an integer array, find a subarray where the sum of numbers is 
zero. Your code should return the index of the first number and the 
index of the last number.

Example:
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].

Note:
there is at least one subarray that is sum up to 0


"""

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    time complexity is O(n^2)

    """
    def subarraySum(self, nums):
        # write your code here
        if not nums or len(nums)==1:
        	return [0,0] 
        for i in xrange(len(nums)):
        	# it's not that trivial, every time we start a new head,
        	# we set it to zero, which corresponds to the inner loop.
        	# first add then compare, then we won't miss the case where 
        	# num[i]=0
        	cur=0
        	for j in xrange(i,len(nums)):
        		cur+=nums[j]
        		if cur==0:
        			return [i,j]


if __name__=='__main__':
	print Solution().subarraySum([-5,0,5,-3,0,1,1,-2,3,-4])


