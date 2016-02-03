"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero

Example:
given array S = {-1 0 1 2 -1 -4}, A solution set is:
(-1, 0, 1)
(-1, -1, 2

Note:
Elements in a triplet (a,b,c) must be in non-descending order.
The solution set must not contain duplicate triplets



"""

class Solution:
	"""
	@param numbersbers : Give an array numbersbers of n integer
	@return : Find all unique triplets in the array which gives the sum of zero.
	"""
	# brutal force way of finding the sum of three numbers
	def threeSum(self, numbers):
		# write your code here
		res=[]
		# sort the sequence first, then fix the head and treat it as 2 sum
		numbers.sort()
		for i in xrange(len(numbers)-2):
			for j in xrange(i+1,len(numbers)-1):
				tmp=numbers[(j+1):]
				if (-numbers[i]-numbers[j]) in tmp:
					if (numbers[i],numbers[j],-numbers[i]-numbers[j]) not in res:
						res.append((numbers[i],numbers[j],-numbers[i]-numbers[j]))
		return res

	# copy from others, notice that the first method we come out is basically the naive 
	# recursion method, then we can dig into the case with less time complexity
	def threeSum2(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
	# Naive method -- O(n^3) solutions
	#     rs = []
	#     self.searchRs(rs, 0, [], nums)
	#     return rs

	# def searchRs(self, rs, level, oneRs, nums):
	#     if level == 3:
	#         if sum(oneRs) == 0:
	#             oneRs.sort()
	#             if oneRs not in rs:
	#                 rs.append(oneRs)
	#         return

	#     for i in range(len(nums)):
	#         newOneRs = oneRs + [nums[i]]
	#         self.searchRs(rs, level+1, newOneRs, (nums[:i] + nums[i+1:]))

		nums.sort()
		target = 0
		rs = []
		newTargetList = []
		for i in range(len(nums)):
			newTarget = target - nums[i]
			if newTarget in newTargetList:
				continue
			else:
				newTargetList.append(newTarget)
			twoRs = self.twoSum(newTarget, nums[:i]+nums[i+1:])
			for row in twoRs:
				row = row + [nums[i]]
				row.sort()
				if row not in rs:
					rs.append(row)
		return rs

# This is the extension of the Two Sum problem, where we have the sorted list and 
# find the two element whose sum is target value
	def twoSum(self, target, nums):
		l = len(nums)
		rs = []
		if l < 2:
			return []

		start = 0
		end = l-1
		while start < end:
			numsSum = nums[start] + nums[end]
			if numsSum == target:
				oneRs = [nums[start], nums[end]]
				if oneRs not in rs:
					rs.append(oneRs)
				start += 1
				end -= 1
			elif numsSum > target:
				end -= 1
			else:
				start += 1
		return rs

		
if __name__=='__main__':
	print Solution().threeSum2([-1,0,1,2,-1,-4])
	print Solution().threeSum([1,-2,1])