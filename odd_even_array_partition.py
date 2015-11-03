#Partition an integers array into odd number first and even number second
# 	example:
# 	Given [1, 2, 3, 4], return [1, 3, 2, 4]

class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        # write your code here
        if not nums:
        	return []
        i=-1
        for j in range(len(nums)):
        	if nums[j]%2 == 0:
        		continue
        	else:
        		i+=1
        		tep=nums[j]
        		nums[j]=nums[i]
        		nums[i]=tep
        return nums

# my first solution passed and it is in place
# 	the way I construct the stucture of this solution is from the quicksort.
# 	we use 2 index to keep track of 2 areas and each of these 2 areas has some functionality.
# 	it is extremely import to understand the partion part using quicksort