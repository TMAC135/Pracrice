# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. 
# The robot is trying to reach the bottom-right corner of the grid 
# (marked 'Finish' in the diagram below).

# Easy danamic programing


class Solution:
	"""
	@param n and m: positive integer(1 <= n , m <= 100)
	@return an integer
	""" 
	def uniquePaths(self, m, n):
		# write your code here
		if m==1 or n==1:
			return 1
#initialization,it's kind of redundent
		# res=[[1]*n]
		# for _ in range(m-1):
		#     row=[1]
		#     for _ in range(n-1):
		#     	row.append(0) 
		#     res.append(row)
# new initialization from others
		res=[[0 for i range(n)] for i in range(m)]
		for i in range(n):
			res[0][i]=1
		for j range(m):
			res[j][0]=1
		for i in range(1,m):
			for j in range(1,n):
				res[i][j]=res[i-1][j]+res[i][j-1]
		return res[m-1][n-1]

if __name__=='__main__':
	a=Solution()
	test=[[2,2],[7,1],[7,7]]
	for i in test:
		print a.uniquePaths(i[0],i[1])