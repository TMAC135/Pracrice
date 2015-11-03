# Follow up for "Unique Paths":
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# Now the input is the matrix which contains bunches of 1's and 0's


# Notoce:
#  	This problem has an implicit requrement,since it can only move downwards and rightwards, then 
# when we initialize the first column and first row, once we encounter a 1, the rest of the column 
# or row will be zeros too since it can't reach the rest with this block in between,this is the bug 
# I have, the ans of test code is 3,but I get 4 without that "break" in line 26 and 32  
class Solution:
	"""
	@param obstacleGrid: An list of lists of integers
	@return: An integer
	"""
	def uniquePathsWithObstacles(self, obstacleGrid):
		# write your code here
		m=len(obstacleGrid)
		n=len(obstacleGrid[0])
		res=[[0 for i in range(n)] for i in range(m)]
		for i in range(n):
			if obstacleGrid[0][i]==1:
				res[0][i]=0
				break #indicate the rest are all zeros
			else:
				res[0][i]=1
		for j in range(m):
			if obstacleGrid[j][0]==1:
				res[j][0]=0
				break    #indicate the rest are all zeros
			else:
				res[j][0]=1
		for i in range(1,m):
			for j in range(1,n):
				if obstacleGrid[i][j]==1:
					res[i][j]=0
				else:
					res[i][j]=res[i-1][j]+res[i][j-1]
		return res[m-1][n-1]

if __name__=='__main__':
	a=Solution()
	test=[[0,0],[0,0],[0,0],[1,0],[0,0]]
	print a.uniquePathsWithObstacles(test)