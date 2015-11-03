"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero

Example:
given array S = {-1 0 1 2 -1 -4}, A solution set is:
(-1, 0, 1)
(-1, -1, 2

Note:
Elements in a triplet (a,b,c) must be in non-descending order.
The solution set must not contain duplicate triplets



"""

class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        res=[]
        # sort the sequence first, then fix the head and treat it as 2 sum
        numbers.sort()
        for i in xrange(len(numbers)-2):
        	for j in xrange(i+1,len(numbers)-1):
        		tmp=numbers[(j+1):]
        		if (-numbers[i]-numbers[j]) in tmp:
        			if (numbers[i],numbers[j],-numbers[i]-numbers[j]) not in res:
        				res.append((numbers[i],numbers[j],-numbers[i]-numbers[j]))
       	return res

if __name__=='__main__':
	print Solution().threeSum([-1,0,1,2,-1,-4])