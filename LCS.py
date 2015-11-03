# Given two strings, find the longest common subsequence (LCS).

# Your code should return the length of LCS.

# Example: 
""""
this is different from the Longst Common Substring, where the characters in Substring
should occur continously in original string.

"""

class Solution:
	"""
	@param A, B: Two strings.
	@return: The length of longest common subsequence of A and B.
	"""

	# 	This is the case we use the matrix to store the length information.
	# it is space cost sice the space complexty is O(m*n)
	def longestCommonSubsequence(self, A, B):
		# write your code here

		if not A or not B:
			return 0
		row=len(A)+1
		column=len(B)+1
		L=[[0 for _ in range(column)] for i in range(row)]
		for i in range (1,row):
			for j in range(1,column):
				if A[i-1] == B[j-1]:
					L[i][j]=1+L[i-1][j-1]
				else:
					if L[i-1][j] >= L[i][j-1]:
						L[i][j] = L[i-1][j]
					else:
						L[i][j] = L[i][j-1]
		return L[row-1][column-1]    

	# we use dictionary to store the longst subsequency words,if we want to return the words 
	# 	information
	def longestCommonSubsequence2(self, A, B):
		# write your code here

		if not A or not B:
			return 0
		row=len(A)+1
		column=len(B)+1
		# use dictionary to store the one optimal solution 
		res={}
		res[0]=''
		L=[[0 for _ in range(column)] for i in range(row)]
		for i in range (1,row):
			for j in range(1,column):
				if A[i-1] == B[j-1]:
					L[i][j]=1+L[i-1][j-1]
					if L[i][j] not in res:
						# these four lines are update the longest words information,every time the 
						# dictionary only hold one key and one value
						key=res.items()[0][0]
						value=res.items()[0][1]
						res={}
						res[L[i][j]]=value+A[i-1]
				else:
					if L[i-1][j] >= L[i][j-1]:
						L[i][j] = L[i-1][j]
					else:
						L[i][j] = L[i][j-1]
		return (L[row-1][column-1],res.items()[0][1])

 
# we can minimize the space complexity to min(row,column),since every time we only 
# need the previous information which is one step before current step

# But We need to make sure the length of A is no less than B then it can give us the 
# min(len(A),len(B)) space complexity.
	def longestCommonSubsequence3(self, A, B):
		# write your code here

		if not A or not B:
			return 0
		row=len(A)+1
		column=len(B)+1
		pre=[0 for _ in range(column)]
		for i in range (1,row):
			cur=[0 for _ in range(column)]
			current=pre[1]
			for j in range(1,column):
				if A[i-1] == B[j-1]:
					cur[j]=pre[j-1]+1
					current=cur[j]
				else:
					if pre[j] >= current:
						cur[j] = pre[j]
					else:
						cur[j] = current
			pre=cur

		return cur[-1]


if __name__=='__main__':
	B='MENTAL'
	A='MATERIAL'
	print Solution().longestCommonSubsequence3(A,B)