# Given a triangle, find the minimum path sum from top to bottom.
# Each step you may move to adjacent numbers on the row below


class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here
        if not triangle:
        	return 0
        if len(triangle)==1:
        	return triangle[0][0]
        if len(triangle)==2:
        	return min(triangle[1][0],triangle[1][1])+triangle[0][0]
       	# initialization for first loop
        a=[triangle[1][0]+triangle[0][0],triangle[1][1]+triangle[0][0]]

        # here actaully I didn't meet the O(n) space requrement since I
        # create the array every time in the loop, the lesson from this experience
        # try to manipulate the array in place.
        for i in xrange(2,len(triangle)):
     # creat every time, space cost. Actually we only need creat once.
        	c=[0 for _ in xrange(len(triangle[i]))] 
        	c[0],c[-1]=a[0]+triangle[i][0],a[-1]+triangle[i][-1]
        	for ii in xrange(1,len(triangle[i])-1):
        		c[ii]=min(a[ii-1],a[ii])+triangle[i][ii]
        	a=c[:]
        return min(a)


class Solution2:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if len(triangle) == 0: return 0
        array = [0 for i in range(len(triangle))]
        array[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i]) - 1, -1, -1):
                if j == len(triangle[i]) - 1:
                    array[j] = array[j-1] + triangle[i][j]
                elif j == 0:
                    array[j] = array[j] + triangle[i][j]
                else:
                    array[j] = min(array[j-1], array[j]) + triangle[i][j]
        return min(array)

if __name__=='__main__':
	test=[[2],[3,4],[6,5,7],[4,1,8,3]]
	print Solution2().minimumTotal(test)



