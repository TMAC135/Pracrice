#coding=utf-8

"""
Given an array of integers, find two non-overlapping subarrays which have the largest sum.
The number in each subarray should be contiguous.

Example
For given [1, 3, -1, 2, -1, 2], the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2], they both have the largest sum 7.

Note
The subarray should contain at least one number

Challenge
Can you do it in time complexity O(n) ?

"""

class Solution:
	"""
	@param nums: A list of integers
	@return: An integer denotes the sum of max two non-overlapping subarrays
	"""

	"""
	first method just use result of maximum_subarray.py, the time complexity
	if O(n^2), thus it it time limit exceed.
	"""
	def maxTwoSubArrays(self, nums):
		# write your code here  
		if not nums: 
			return 0
		if len(nums)==1:
			return nums[0]
		# left,right=[],[]
		res=-999999999
		for i in xrange(len(nums)):
			left=self.maxSubArray(nums[:(i+1)])
			right=self.maxSubArray(nums[(i+1):])
			if (left+right)>res:
				res=left+right
		return res


	def maxSubArray(self, nums):
		# write your code here
		thissum=0
		maxsum=-99999999999
		for i in nums:
			if thissum<0:
				thissum=0
			thissum+=i
			maxsum=max(maxsum,thissum)
		return maxsum
	"""
	method 2: time complexity O(n)
	Notice it is good extention of maximum_subarray.py,
	we use forwards and backwards traversal to record the global 
	max of the left block and right block at each element in the array.
	我们的目的是当遍历整个数列时，有左边的数列的最大字序列和右边数列的最大子序列和，但如果
	每次都调用 maxSubArray 方法时，如method1, 时间复杂度会是O(n^2)。
	forwards and backwards traversal 会减少时间复杂度。

	"""
	def maxTwoSubArrays2(self, nums):
		# write your code here  
		if not nums: 
			return 0
		if len(nums)==1:
			return nums[0]
		# find the global max for left block
		left_max=[]
		Max=-9999999
		thissum=0
		for i in xrange(len(nums)):
			if thissum<0:
				thissum=0
			thissum+=nums[i]
			Max=max(Max,thissum)
			left_max.append(Max)
		# return left_max
		# same method apply to the right block
		right_max=[]
		Max=-9999999
		thissum=0
		for i in xrange(len(nums)-1,-1,-1):
			if thissum<0:
				thissum=0
			thissum+=nums[i]
			Max=max(Max,thissum)
			right_max.append(Max)
		# return right_max
		# be careful of the index of right_max matrix since 
		# it travel backwards
		res=-999999999
		for i in xrange(len(nums)-1):
			res=max(res,left_max[i]+right_max[len(nums)-i-2])
		return res



if __name__=='__main__':
	print Solution().maxTwoSubArrays2([1,3,-1,2,-1,2])


