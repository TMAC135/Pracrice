#coding=utf-8

"""
Given a list of numbers with duplicate number in it. Find all unique permutations.

Example
For numbers [1,2,2] the unique permutations are:

[

    [1,2,2],

    [2,1,2],

    [2,2,1]

]

Challenge
Do it without recursion.

"""

class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """

    """
    First use recursion.A slight change from the non duplicte case, we are keeping 
    comparing the current value with previous value, if it is the same, then we 
    can jump to the next value since we already consider all permutation cases 
    in the previous value.

    """

    def permuteUnique(self, nums):
        # write your code here
        if not nums:
        	return []
        nums.sort()
        res=[]
        self.dfs(nums,[],res)
        return res



    def dfs(self,nums,tmp,res):

    	if not nums:
    		res.append(tmp)
    	prev=None
    	for i in xrange(len(nums)):
    		if nums[i] != prev:
    			self.dfs(nums[:i]+nums[(i+1):],tmp+[nums[i]],res)
    		prev=nums[i]

    """
    Non recursive way

    """
    def permuteUnique2(self, nums):
        # write your code here
        if not nums:
        	return []
        nums.sort()
        res = [[]]
        for _ in xrange(len(nums)):
        	# prev=None
        	tmp=[]
        	prev=None
        	for a in nums:
        		
        		for b in res:
        			if a!=prev:
        				if a not in b:
        					tmp += [[a]+b]
        		prev=a


        	res=tmp
        return res


if __name__ == '__main__':

	print Solution().permuteUnique2([1,2,2])	









