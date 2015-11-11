#coding=utf-8

"""
Given a list of numbers, return all possible permutations.

Example
For nums = [1,2,3], the permutations are:

[
	[1,2,3],
	[1,3,2],
	[2,1,3],
	[2,3,1],
	[3,1,2],
	[3,2,1]
]

Challenge
Do it without recursion.

"""

class Solution:
		"""
		@param nums: A list of Integers.
		@return: A list of permutations.
		"""
		# Method 1#
		"""
		The recursion method, we keep recursion in the subset. Similar to the 
		subset problem, but notice the base case for this method.

		"""
		def permute1(self, nums):
				# write your code here
				res=[]
				self.recursion(nums,[],res)
				return res


		def recursion(self,nums,tmp,res):
			if not nums:
				res.append(tmp)

			for i in xrange(len(nums)):
				# nums[0],nums[i]=nums[i],nums[0];
				self.recursion([x for x in nums if x!=nums[i]],tmp+[nums[i]],res)

		# Method 2#
		# use non recursive way, the idea is similar to the BFS,we firstly generate
    # all possible permutations at current depth, we keep adding the elements.

    """
    事实上这种permutation 的方法可以拓展，例如给定一个list,返回两两permutation
    的所有结果，我们就可以将下面的 xrange(len(nums)) 改成 xrange(2), general 的 情况
    是k.
    此题是特例，我们一直求k=len(nums)的情况


    """ 
		def permute2(self,nums):

			if not nums:
				return []
			res=[[]]
			for _ in xrange(len(nums)):
				res=[[a] + b for a in nums for b in res if a not in b]
			return res

			# k<=len(nums)
		def permute2(self,nums，k):

			if not nums:
				return []
			res=[[]]
			for _ in xrange(k):
				res=[[a] + b for a in nums for b in res if a not in b]
			return res





if __name__=='__main__':
	print len(Solution().permute1([1,2,3,4]))




