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
    
    def permute2(self,nums):



if __name__=='__main__':
	print Solution().permute1([1,2,3])




