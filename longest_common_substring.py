"""
Given two strings, find the longest common substring.Return the length of it.

Example:
Given A = "ABCD", B = "CBCE", return 2.

Note:
The characters in substring should occur continuously in original string. This is different with subsequence.

Challenge:
O(n x m) time and memory.
"""

class Solution:
	"""
	Also see LCS, the core of thoughts is different
	"""
	# @param A, B: Two string.
	# @return: the length of the longest common substring.
	def longestCommonSubstring(self, A, B):
		# write your code here

		if not A or not B:
			return 0
		# LA=list(A)
		# LB=list(B)
		res=0
		for i in xrange(len(A)):
			res=max(self.compare(A[i:],B),res)
		return res

# 	this is the subproblem from the original problem, every time we fixed the 
# head point of the string, and extract the maximum length of this common substring 
# given this fixed head.
	def compare(self,A,B):
		# we need a list to store the common length information. 
		cur=[0]
		LA=list(A)
		com=LA.pop(0)
		for i in xrange(len(B)):
			if B[i]==com:
				cur[-1]+=1
				if LA:
					com=LA.pop(0)
				else:
					return len(A)
		# this is the case where we start a new compare 
			elif cur[-1]>0:
				cur.append(0)
				LA=list(A)
				com=LA.pop(0)
		return max(cur)

if __name__=='__main__':
	print Solution().longestCommonSubstring("ja;jfadflakjdfa;djfadfdnvadbfkbH:DADHFLDSHfakldhflakdf;adfasdhfaufhakdbalbgaldbalkdfafhalkdsfhalsdufhakldbakladshfuojfanjoiehflakshf", "adfanbajfasdjfaodjfaldfnasldfjao")



