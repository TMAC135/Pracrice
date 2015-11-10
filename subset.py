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
		# call the list to be added valuelist
		if s:
			for i in xrange(len(s)):
				res.append(tmp+[s[i]])
				self.dfs(s[(i+1):],tmp+[s[i]],res)

	# Method of Bit manipulation

	"""
	Copy from others solution, use bit manipulation:
	相当牛逼的bit解法。基本的想法是，用bit位来表示这一位的number要不要取，第一位有1，0即取和不取2种可能性。所以只要把0到N种可能
	都用bit位表示，再把它转化为数字集合，就可以了。
	http://www.fusu.us/2013/07/the-subsets-problem.html

	"""
	def subsets2(self, S):
		S.sort()
		k = len(S)
		n = 2 ** k
		res = []
		for i in range(n):
			s = self.filter(S, k, i)
			res.append(s)
		return res

	"""
	这个filter 函数可以拓展为任意的 bit select 问题，给定一个list,长度是k,我们输入任意
	数字 0 <= i <= 2^k - 1, 可以表示为长度为k的二进制表达式， 若该位为0，则不选择，
	若为1则选择。
	"""
	def filter(self, S, k, i):
		res = []
		for j in range(k):
			mask = 1 << j
			if i & mask > 0:
				res.append(S[j])
		return res

	# Method of Interation
	"""
	First, consider there is no duplicates, how to generate the subsets?
	Say n is the # of the elements,
	when n=1, subsets :  {}, {"1"},  "i" means the ith element.
	when n=2, subsets:   {}, {"1"}, {"2"}, {"1", "2"}
	when n=3, subsets:   {}, {"1"}, {"2"}, {"1", "2"}, {"3"}, {"1","3"}, {"2","3"}, {"1", "2","3"}
	So, the way of generating subsets is:
	for current element, add this element to all the subsets list in the res

	"""

	def subsets3(self,S):
		if not S:
			return S
		S.sort()
		res=[[]]
		for i in S:
			add=[x+[i] for x in res]
			res+=add
		return res





if __name__=='__main__':
	print Solution().subsets3([1,3,2]);





