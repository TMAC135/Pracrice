# Given an array of integers, the majority number is the number 
# that occurs more than 1/3 of the size of the array

# Example: Given [1, 2, 1, 2, 1, 3, 3], return 1

# challenge: O(n) time and O(1) extra space

class Solution:
    """
    @param nums: A list of integers
    @return: The majority number occurs more than 1/3

    this is similar to the majority number I, now we need to store 2 possible 
    candidate since the true majority only greater than 1/3 of the total size
    see the reference:  http://www.cnblogs.com/yuzhangcmu/p/4175779.html
    """
    def majorityNumber(self, nums):
        # write your code here
        num1=None
        num2=None
        con1=0
        con2=0
        for i in nums:
        	if i in (num1,num2):
        		if num1==i:
        			con1+=1
        		else:
        			con2+=1
        	else:
        		if con1==0:
        			num1=i
        			con1=1
        		elif con2==0:
        			num2=i
        			con2=1
        		else:
        			con1-=1
        			con2-=1
        # we still need to check the last 2 candidates num1 and num2
        # 	 filter in python is pretty useful to choose the specific value we want to choose(powerful)
        if len(filter(lambda x:x==num1,nums))>len(nums)/3:
        	return num1
        else:
        	return num2

