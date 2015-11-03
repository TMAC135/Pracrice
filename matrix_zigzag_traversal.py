# Given a matrix of m x n elements (m rows, n columns), 
# return all elements of the matrix in ZigZag-order.

"""
Given a matrix:
[
  [1, 2,  3,  4],
  [5, 6,  7,  8],
  [9,10, 11, 12]
]
return [1, 2, 5, 9, 6, 3, 4, 7, 10, 11, 8, 12]


"""

class Solution:
    # @param: a matrix of integers
    # @return: a list of integers

    """
    the trick here is that we the sum of row and column index is the same when
    we keep walking the oblique line. Also notice that we the number of 
    walk we traver is m+n, this is the criteria we set for testing the 
    end of the loop.
    总体来说，我们通过规律发现，当i为偶数，我们斜着向上遍历，奇数时斜向下遍历，然后
    对于每一个i设定边界条件即可。
    """
    def printZMatrix(self, matrix):
        # write your code here
	if not matrix:
		return []
	m=len(matrix)
	n=len(matrix[0])
	i=0
	# zig=0
	res=[]
	for i in xrange(m+n):
		if (i%2)==0:
			for j in xrange(i+1):
				if j<n and i-j<m:
					res.append(matrix[i-j][j])
			# i+=1
		else:
			for j in xrange(i,-1,-1):
				if j<n and i-j<m:
					res.append(matrix[i-j][j])
		i+=1
	return res



if __name__=='__main__':
	test=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
	print Solution().printZMatrix(test)