# coding=utf-8

"""
Given a matrix of m x n elements (m rows, n columns), 
return all elements of the matrix in spiral order.

Example
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

"""
"""
boundary conditions are so annoy, 不用下面的解法
"""
class Solution:
	# @param {int[][]} matrix a matrix of m x n elements
	# @return {int[]} an integer array
	def spiralOrder1(self, matrix):
		# Write your code here
		def recursion(mat,res):
			if len(mat)>1:
				row = len(mat)
				column = len(mat[0])
				if column>1:


					first_row = mat[0][:]
					last_row = mat[-1][:]
					first_column = [mat[i][0] for i in xrange(1,row-1)]      		
					last_column = [mat[i][-1] for i in xrange(1,row-1)]

					"""
					notice we can't add since we will change the id of res so we are not operate in the original space for res
					"""
					# res = res + first_row + last_column + last_row[::-1] + first_column[::-1] #wrong
					tmp = first_row + last_column + last_row[::-1] + first_column[::-1]
					res.extend(tmp)

					# return res
					mat = [[mat[i][j] for j in range(1,column-1)] for i in range(1,row-1)]
					if mat:	
						recursion(mat,res)
				else:
					tmp = []
					for i in mat:
						tmp += i
					res.extend(tmp)
			else:
				res.extend(mat[0])
				# return res
		if not matrix:
			return []
		res = []
		recursion(matrix,res)
		return res
		return res
	"""
	Good trick for the variable direct, Notice the terminal case
	for the while loop
	"""

	def spiralOrder(self, matrix):
		if matrix == []: return []
		up = 0; left = 0
		down = len(matrix)-1
		right = len(matrix[0])-1
		direct = 0  # 0: go right   1: go down  2: go left  3: go up
		res = []
		while True:
			if direct == 0:
				for i in range(left, right+1):
					res.append(matrix[up][i])
				up += 1
			if direct == 1:
				for i in range(up, down+1):
					res.append(matrix[i][right])
				right -= 1
			if direct == 2:
				for i in range(right, left-1, -1):
					res.append(matrix[down][i])
				down -= 1
			if direct == 3:
				for i in range(down, up-1, -1):
					res.append(matrix[i][left])
				left += 1
			if up > down or left > right: return res
			direct = (direct+1) % 4

if __name__ == '__main__':
	print Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) 
	print Solution().spiralOrder1([[1,2],[3,4]])


