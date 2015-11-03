"""
Print numbers from 1 to the largest number with N digits by recursion.

Example:
Given N = 1, return [1,2,3,4,5,6,7,8,9].
Given N = 2, return [1,2,3,4,5,6,7,8,9,10,11,12,...,99]
"""


class Solution:
	# @param n: An integer.
	# return : A list of integer storing 1 to the largest number with n digits.
	def numbersByRecursion(self, n):
		# write your code here
		if n<=0:
			return []
		res=[]
		self.recursion(n,res)
		return res[::-1]

	def recursion(self,n,res):
		if n>=1:
			for i in xrange(10**n-1,10**(n-1)-1,-1):
				res.append(i)
			self.recursion(n-1,res)		