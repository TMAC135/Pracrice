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

	# Method of recursion
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


	# Method of Interation
	"""
	Then we take the duplicates into account, the same example:
	when n=1, subsets :  {}, {"1"},  "i" means the ith element.
	when n=2, subsets:   {}, {"1"}, {"2"}, {"1", "2"}
	when n=3, but "2"=="3" subsets: 
	   {}, {"1"}, {"2"}, {"1", "2"}, {"3"}, {"1","3"}, {"2","3"}, {"1", "2","3"}
	since "2"=="3", which truly is:
	   {}, {"1"}, {"2"}, {"1", "2"}, {"2"}, {"1","2"}, {"2","2"}, {"1", "2","2"}
	where the bold ones are not needed.
	So, how these two subsets are generated? They are from the subsets of n=1.

	In sum up, when meet the same element as previous one, then generate new subsets ONLY 
	from the subsets generated from previous iteration, other than the whole subsets list.
	"""

	def subsetsWithDup2(self,S):
		if not S:
			return S
		S.sort()
		res=[[]]
		# prev_add is used to deal with the case of current element is same as previous one
		prev_add=[]
		prev=None
		for i in xrange(len(S)):
			if S[i] != prev:
				add = [ x + [S[i]] for x in res]
			else:
				add = [ x + [S[i]] for x in prev_add] # if the same, we can only add the element from previous add
			res += add
			prev_add=add
			prev=S[i]
		return res

if __name__=='__main__':
	print Solution().subsetsWithDup2([1,1,2,2])



