"""
Given an array S of n integers, find three integers in S such that the sum 
is closest to a given number, target. Return the sum of the three integers.

Example:
For example, given array S = {-1 2 1 -4}, and target = 1. The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Note:
You may assume that each input would have exactly one solution.

Challenge:
O(n^2) time, O(1) extra space

"""

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.\

    Solution from others, i am struggling with how to implement it O(N^2) time.
    I know we need to sort the array first but don't know how to pass throght the 
    array. 

    here are several key point for these problem, mindif is to store the minimim diffences 
    value and corresponsdingly the minimum sum is in res. The sum is used to 
    judge which pointer we should move, since we already sort the array. if the 
    sum > target, we may reduce the right pointer since it produce less value for the 
    next iteration. Similarly to the case where sum > target. Thus we are making sure 
    we use O(N) time in the second loop.

    The beauty of this method is we use the sorted information to reduce O(N^3) to 
    O(N^2) time. The reason is just anylyzed above.  

    """
    def threeSumClosest(self, numbers, target):
        # write your code here
		if not numbers or len(numbers)<3:
			return None
		numbers.sort()
		# initial value of minimum difference
		mindif=1000000000
		res=0
		for i in xrange(len(numbers)):
			left=i+1
			right=len(numbers)-1
			while(left<right):
				sum=numbers[i]+numbers[left]+numbers[right]
				diff=abs(sum-target)
				if diff<mindif:
					mindif=diff
					res=sum
				if sum==target:
					return sum
				elif sum>target:
					right-=1
				else:
					left+=1

		return res



if __name__=='__main__':
	print Solution().threeSumClosest([-1,2,1,-4],1)
