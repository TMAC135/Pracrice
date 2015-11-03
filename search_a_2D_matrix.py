"""
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row


Example:
[
	[1, 3, 5, 7],
	[10, 11, 16, 20],
	[23, 30, 34, 50]
]
Given target = 3, return true.

Challenge
O(log(n) + log(m)) time
"""

class Solution:
	"""
	@param matrix, a list of lists of integers
	@param target, an integer
	@return a boolean, indicate whether matrix contains target

	Not that easy as it seems, we need to be clear about the initial condition
	for the binary search, I seperate the matrix into 2 binary search in a array.

	The solution from other is just binary search in the matrix. 

	"""
	def searchMatrix(self, matrix, target):
		# write your code here
		if not matrix:
			return False
		head=[i[0] for i in matrix]
		s=0
		e=len(head)-1
		while(s<e):
			m=(s+e)/2+1
			if head[m]==target:
				return True
			elif head[m]>target:
				e=m-1
			else:
				s=m
		# return s
		search=matrix[s]
		if search[0]>target:
			return False
		if search[-1]<target:
			return False
		ss=0
		ee=len(search)-1
		while(ss<ee-1):
			mm=(ss+ee)/2
			if search[mm] == target:
				return True
			elif search[mm] > target:
				ee=mm
			else:
				ss=mm

		return True if search[ee] == target or search[ss]==target else False

class Solution2:
	# @param matrix, a list of lists of integers
	# @param target, an integer
	# @return a boolean
	"""
	Again, the method here is similar to the search a 2D matrix II.
	It is different from my version but it is more simple and concise, this method 
	is based on the sorting information in the problem. 

	Notice we start our walk from the upright of the matrix.

	"""
	def searchMatrix(self, matrix, target):
		if not matrix:
			return False
		i = 0; j = len(matrix[0]) - 1
		while i < len(matrix) and j >= 0:
			if matrix[i][j] == target: return True
			elif matrix[i][j] > target: j -= 1
			else: i += 1
		return False


if __name__=='__main__':
	print Solution2().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],0.2)


