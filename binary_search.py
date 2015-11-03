"""
For a given sorted array (ascending order) and a target number, 
find the first index of this number in O(log n) time complexity.
If the target number does not exist in the array, return -1.

Example
If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.

Challenge
If the count of numbers is bigger than 2^32, can your code work properly?


"""

class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        if not nums or nums[0]>target or nums[-1]<target:
        	return -1
        s=0
        e=len(nums)-1
        while s<e-1:
        	m=(s+e)/2
        	if nums[m]>=target:
        		e=m
        	else:
        		s=m
        if nums[s]==target:
        	return s
        elif nums[e]==target:
        	return e
        else:
        	return -1


if __name__=='__main__':
	print Solution().binarySearch([1,2,3,3,4,5,10],10)








