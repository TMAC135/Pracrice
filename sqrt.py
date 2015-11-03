# Implement int sqrt(int x).
# Compute and return the square root of x.

# Example: sqrt(3)=1,sqrt(4)=2

# Challenge: O(log(x))



class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    this is the typical binary search problem, the only thing we need to pay attention to is 
    to check the final contion, the information here is sqrt(5)=2 not 3, thus we made the 
    mid = (start + end) / 2 
    """
    def sqrt(self, x):
        # write your code here
        if x<0:
        	return None
        start=0
        end=x
        while(end!=start):
        	mid = (start+end)/2 +1 
        	if mid**2 == x :
        		start=mid
        		break
        	elif mid**2 > x:
        		end = mid-1
        	else:
        		start = mid
        return start 

if __name__=='__main__':
	test = [0,1,4,5,100,101,402]
	for i in test:
		print Solution().sqrt(i)