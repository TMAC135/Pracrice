#coding=utf-8

"""
Given a list of numbers that may has duplicate numbers, return all possible subsets

Example
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

Note
Each element in a subset must be in non-descending order.
The ordering between two subsets is free.
The solution set must not contain duplicate subsets

Challenge
Can you do it in both recursively and iteratively?
"""

class Solution:
	"""
	@param S: A set of numbers.
	@return: A list of lists. All valid subsets.

	this method base on the subset.py, we only consider the case where 
	"""

	def subsetsWithDup(self, S):
		# write your code here
		S.sort()
		res=[[]]
		self.dfs(S,[],res)
		return res


	def dfs(self,s,tmp,res):
		prev=None
		if s:
			for i in xrange(len(s)):
				if s[i]!=prev:
					res.append(tmp+[s[i]])
					self.dfs(s[(i+1):],tmp+[s[i]],res)
					prev=s[i]


if __name__=='__main__':
	print Solution().subsetsWithDup([1,2,2])



