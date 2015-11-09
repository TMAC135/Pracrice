#coding=utf-8

"""
Given a set of distinct integers, return all possible subsets.

Example
If S = [1,2,3], a solution is:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

Note
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.

Challenge
Can you do it in both recursively and iteratively?

"""


class Solution:
	"""
	@param S: The set of numbers.
	@return: A list of lists. See example.

	"""

	# Method of Recursion, it takes me some time to figure it out
	# Notice that we need a list res to store all the results
	# we also need a list tmp to add elements base on the previous information.
	"""
	show byexample:
				     [ ]      	  tmp,s=[],[1 2 3]
				   /  \  \
				[1]  [2]  [3]     tmp,s=[],[1 2 3] ; [],[2 3]  ; [],[3]
			   /  \     \
			[1 2] [1 3]  [2,3]    tmp,s=[1],[2 3] ; [2],[3] ; [3],[]
			/
		   [1 2 3]                tmp,s=[1 2],[3]
	""" 
	def subsets1(self, S):
		S.sort()
		res=[[]]
		self.dfs(S,[],res)
		return res


	def dfs(self,s,tmp,res):
		if s:
			for i in xrange(len(s)):
				res.append(tmp+[s[i]])
				self.dfs(s[(i+1):],tmp+[s[i]],res)

	# Method of Interation
	def subsets2(self,S):






if __name__=='__main__':
	print Solution().subsets1([1,3,2]);






