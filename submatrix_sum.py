# Given an integer matrix, find a submatrix where 
# the sum of numbers is zero. Your code should return the coordinate 
# of the left-up and right-down number

# example:
# [[1,5,7],[3,7,-8],[4,-8,9]], return [(1,1),(2,2)]


# my solution, which pass 8 cases,and end up with time limit exceeded.
# class Solution:
# 	def submatrixSum(self,matrix):
# 		if not matrix:
# 			return []
# 		row=len(matrix)
# 		coloum=len(matrix[0])
# 		index = []
# 		try:
# 			for i in xrange(row):
# 				for j in xrange(coloum):
# 					left=(i,j)
# 					for ii in range(i,row):
# 						for jj in range(j,coloum):
# 							right=(ii,jj)
# 							if self.Sum([left,right],matrix) == 0:
# 								index = [left,right]
# 								raise IndexError
# 		except:
# 			return index
# 		return [(-1,-1),(-1,-1)]



# 	def Sum(self,index,matrix):
# 		sum = 0
# 		for i in xrange(index[0][0],index[1][0]+1):
# 			for j in xrange(index[0][1],index[1][1]+1):
# 				sum+=matrix[i][j]
# 		return sum
    # @param {int[][]} matrix an integer matrix
    # @return {int[][]} the coordinate of the left-up and right-down number

# The difficulty part for this problem is how to complete this program in O(n^3)
# 	time, if we are trying to fix the topleft and bottomright points, then we need 4 for 
# 	loops thus it will O(n^4)time, 
#The tricky here been used is to process the previous matrix first, like we can sum up all the
# 	coloum in the corresponding index, it will provide convinience when we use sum the submatrix.
# 	then we use the i and j to represent the row_top and row_bottom and then scan the matrix in betweem
# 	h here play an import role to record the sum information in the previous matrixs, if we find the 
# 	same sum in h, which means we must have submatrix in between that sum up to 0, 

class  Solution:
	"""docstring for  """
	def submatrixSum(self,matrix):
		if not matrix:
			return []
		coloum=len(matrix[0])
		row=len(matrix)
		new_mat= [[0 for _ in range(coloum+1)]for _ in range(row+1)]
		for i in range(coloum):
			for j in range(row):
				new_mat[j+1][i+1]=matrix[j][i]+new_mat[j][i+1]
		# for ii in range(row):
		# 	for jj in range(coloum):
		# 		new_mat[ii+1][jj+1]+=new_mat[ii+1][jj]
		for i in range(1,row+1):
			for j in range(i,row+1):
				h={}
				h[0]=0
				s=0
				for down in range(1,coloum+1):
					s += new_mat[j][down]-new_mat[i-1][down]
					if s in h:
						return [(i-1,h[s]),(j-1,down-1)]
					h[s]=down
		return [(-1,-1),(-1,-1)]
if __name__ == '__main__':
	assert Solution().submatrixSum([[1,5,7],[3,7,-8],[4,-8,9]])\
	==[(1,1),(2,2)]












		

	