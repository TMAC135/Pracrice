# Given an array of integers, the majority number is the number 
# that occurs more than half of the size of the array. Find it.

# Example : 
# Given [1, 1, 1, 1, 2, 2, 2], return 1

# chanllenge: O(n)time and O(1) extra space


# Use of the hash table,but it use the O(n) space, it's unacceptable
# class Solution:
#     """
#     @param nums: A list of integers
#     @return: The majority number
#     """
#     def majorityNumber(self, nums):
#         # write your code here
#         if not nums:
#         	return None
#         if len(nums)==1:
#         	return nums[0]
#         d={}
#         for i in nums:
#         	if i in d:
#         		d[i]+=1
#         	else:
#         		d[i]=1
#         list=d.items()
#         for i in list:
#         	if i[1]>(len(nums)/2):
#         		return i[0]
#         return False


# this methos use O(1) space 
class Solution:
    def majorityNumber(self, nums):
        """
        Moore's Voting Algorithm
        greedy half
        :param nums: A list of integers
        :return: The majority number
        """
        cnt = 0
        maj = 0
        for ind, num in enumerate(nums):
            if num == nums[maj]:
                cnt += 1
            else:
                cnt -= 1  # every time --, discard 2 different numbers

            if cnt < 0:
                maj = ind
                cnt = 1

        # assured that the majority exists, otherwise need to double check
        return nums[maj]

if __name__=='__main__':
	a=Solution()
	test=[[1,1,1,1,2,2],[1,2],[2,2,3,3,3,1,1,1,1],[2]]
	for i in test:
		print a.majorityNumber(i)