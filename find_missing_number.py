#Given an array contains N numbers of 0 .. N, find which number doesn't exist in the array.
#Given N = 3 and the array [0, 1, 3], return 2.

class Solution:
    # @param nums: a list of integers
    # @return: an integer
    def findMissing(self, nums):
        # write your code here
        if not nums:
        	return 0
        nums.append(-1) #same idea as find_missing_positive
        nums.sort()
        val = 0   #we use val to track the possible missing number, and we should deal with the 
        		  #reated case like [0,0,0,1,2]
        for i in xrange(1,len(nums)):
        	if nums[i] != nums[i-1]:
        		val += 1
        		if nums[i] != val-1:
        			return val-1 
        return len(nums)-1 # because we add an extra entry, this is the case for [0,1,2,3]
        					#which we lack the last number of the N number
