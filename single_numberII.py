# Given 3*n + 1 numbers, every numbers occurs triple times except one, find it

# example: Given [1,1,2,3,3,3,2,2,4,1] return 4

class Solution:
    """
	@param A : An integer array
	@return : An integer
	main reference: http://www.cnblogs.com/zuoyuan/p/3719753.html
		the main thought behind this is to count the number of 1's in every bit, since 
		problem says only one number occurs once and others occurs triple times, then we 
		can module 3 every time for every bit. then the remaining after one pass 
		is the number we want.
		To implement the 3-count strategy in binary, use 2 bits to store the count, 00,01,10,11
		once we hit 11, we will reset both bits to 0 ,which is 00. 
	In general, if the problem is related to the counts of numbers, bit manipulations is a
		possible way to explore
    """
    def singleNumberII(self, A):
        # write your code here
        if not A:
        	return 0
        #  one and two is the combinations for counting the 1's in the corresponding bit,the reason for 
        # 	use 2 bit is related to 3, if other number appear more than 3 times, we need more bits
        one,two,three=0,0,0
        for i in A:
        	two |= (i&one)
        	one = one^i
        	# In the certain bit i , if one[i]=two[i]=0,we need to reset to 0, ohterwise we need to 
        	# 	remain the same
        	three = one^two
        	one &=three
        	two &=three
        # from the problem, only one number appear once, thus one is the final answer.
        return one

if __name__=='__main__':
	print Solution().singleNumberII([1,1,2,3,3,3,2,2,4,1])

# Another brilliant method, it is highly relying on the problem, we first assume all number 
# 	appear triple times, then (sum of these triple times number) - (sum of the original number) 
# 	should be that (unique number * 2),
# This method is perfectly suit for the application of set, since set is combination 
# 	of unrepeated elements.
# However,this method is easy to overflow if the number is too big

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        a= set(nums)
        a = sum(a)*3 -sum(nums)
        a = a/2
        return a























        