#coding=utf-8
"""
Given an array of integers, find a contiguous subarray which has the largest sum.

Example
Given the array [−2,2,−3,4,−1,2,1,−5,3], the contiguous subarray [4,−1,2,1] has the largest sum = 6

Note
The subarray should contain at least one number.

Challenge
Can you do it in time complexity O(n)?
"""


class Solution:
	"""
	@param nums: A list of integers
	@return: An integer denote the sum of maximum subarray

	the method is very subtle and keep discard the negative sum,actually 
	this method is DP problem. 

	Difine Max(i) as the maximum sum of A(0,i) in the range [k,i] , 0<=k<=i
	then Max(i+1)=Max(i)+A[i+1] if Max(i+1) >=0. else it indicate the 
	sum with the ending i+1 is negative, then we can redifine Max(i+1) is 0.

	Notice that the if all elements in the lists are negative, we should take 
	care of that and the OJ doesn't consider that. 

	另一种解释很好：假设我们已知第i步的global[i]（全局最优）和local[i]（局部最优），那么第i+1步的表达式是：
	local[i+1]=Math.max(A[i], local[i]+A[i])，就是局部最优是一定要包含当前元素
	"""
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

	# try to list the maximum subarray numbers
	"""
	it cause me some time to come up with this way, we always 
	keep walking forwar, but we need to record the possible start 
	point of the array, that is the function of cur. It updates the time 
	as the thissum value is less than 0.
	"""

	def maxSubArray2(self,nums):
		thissum=0
		s=0 # s is the true start of the maximum subarray
		e=0 # e is the true start of the maximum subarray
		cur=0 # cur is the possible start point. 
		maxsum=-99999999999
		for i in xrange(len(nums)):
			if thissum<0:
				thissum=0
				cur=i
			thissum+=nums[i]
			if maxsum<thissum:
				s=cur
				e=i
				maxsum=thissum

		return (maxsum,s,e)




	# use divide and conquer to solve, time complexity O(nlogn)
	def maxSubArray3(self,nums):
		return 0



if __name__=='__main__':
	print Solution().maxSubArray([-1])



