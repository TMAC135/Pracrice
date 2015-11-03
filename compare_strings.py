# Compare two strings A and B, determine whether A contains all of the characters in B.
# The characters in string A and B are all Upper Case letters.

# Example: 
# For A = "ABCD", B = "ACD", return true
# For A = "ABCD", B = "AABC", return false

class Solution:
	"""
	@param A : A string includes Upper Case letters
	@param B : A string includes Upper Case letters
	@return :  if string A contains all of the characters in B return True else return False

	I use the list as a tool to deal with the string manipulations, since strings are inmutable
	Besides, I also use "i in list_a" which is in python.
	"""
	def compareStrings(self, A, B):
		# write your code here

		if not A:
			return True
		if not B:
			return False

		list_b=list(B)
		list_a=list(A)
		for i in list_b:
			if i in list_a:
				list_a.remove(i)
			else:
				return False
		return True


# here is the solution from others, it is very efficient
# use only O(1) space and linear time.
# 	To be more general, for the problem about the ASICII characters, we can map them to the
# real arrays and it just cost O(1) space - 256. Usually the manipulations on the real array will
# be more convinient in terms of character. 
class Solution2:
	def compareStrings(self, A, B):
		"""
		Straightforward
		:param A : A string includes Upper Case letters
		:param B : A string includes Upper Case letters
		:return :  if string A contains all of the characters in B return True else return False
		"""
		cnt = [0 for _ in xrange(26)]
		for c in A:
			cnt[ord(c)-ord('A')] += 1
		for c in B:
			cnt[ord(c)-ord('A')] -= 1
			if cnt[ord(c)-ord('A')]<0:
				return False
		return True


if __name__=='__main__':
	A='ABCD'
	B='AABC'
	print Solution2().compareStrings(A,B)


