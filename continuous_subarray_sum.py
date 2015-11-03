# Given an integer array, find a continuous subarray where the
 # sum of numbers is the biggest. Your code should return the index
  # of the first number and the index of the last number. 
  # (If their are duplicate answer, return anyone)

  # example: [-3,1,3,-3,4],return [1,4]

# the solution in the textbook, time limit exceed.
# class Solution:
#     # @param {int[]} A an integer array
#     # @return {int[]}  A list of integers includes the index of the 
#     #                  first number and the index of the last number
#     def continuousSubarraySum(self, A):
#         # Write your code here
#         if not A:
#         	return []
#         # A.insert(0,0)
#         return [self.max_subarray(A,0,len(A)-1)[0],self.max_subarray(A,0,len(A)-1)[1]]

#     def max_subarray(self,A,start,end):
#     	if start == end:
#     		return [start,end,A[start]]
#     	# elif start == end -1:
#     	# 	if A[start]<=A[end]:
#     	# 		return [end,end,A[end]]
#     	# 	else:
#     	# 		return [start,start,A[start]]

#     	mid = (end+start)/2
#     	comb=[self.max_subarray(A,start,mid),\
#     	self.max_subarray(A,mid+1,end),self.max_subarray_between(A,start,mid,end)]
#     	number = [comb[i][2] for i in range(3)]
#     	return comb[number.index(max(number))]

#     def max_subarray_between(self,A,start,mid,end):
#     	left_sum = -99999999
#     	sum=0
#     	for i in range(mid,start-1,-1):
#     		sum+=A[i]
#     		if left_sum<sum:
#     			left_sum=sum
#     			left_index=i
#     	right_sum=-99999999
#     	sum=0
#     	for j in range(mid+1,end+1):
#     		sum+=A[j]
#     		if right_sum<sum:
#     			right_sum=sum
#     			right_index=j
#     	return [left_index,right_index,left_sum+right_sum]



# if __name__ == '__main__':
# 	assert Solution().continuousSubarraySum([-1,1])\
# 	==[1,1]

from collections import namedtuple
Sum = namedtuple("Sum", "sum i j")  # data structure to store the sum and the starting and ending index.


class Solution:
    def continuousSubarraySum(self, A):
        """
        Break at 0
        :param A: an integer array
        :return: A list of integers includes the index of the first number and the index of the last number
        """
        if len(A) < 1:
            return [-1, -1]

        ret = Sum(A[0], 0, 0)
        cur = 0  # current sum
        s = 0
        for e, v in enumerate(A):
            cur += v
            if ret.sum < cur:
                ret = Sum(cur, s, e) #we will update our result only when we have a larger sum.

            if cur < 0:  #if previous around sum is negtive, 
            # it can't contibute to the maximum array,so we need to start a new round
                s = e+1
                cur = 0

        return [ret.i, ret.j]


if __name__ == "__main__":
    assert Solution().continuousSubarraySum(
        [-101, -33, -44, -55, -67, -78, -101, -23, -44, -55, -67, -78, -100, -200, -1000, -22, -100, -200, -1000, -22]
    ) == [15, 15]


# Obciously, other's code is much simpler than mine. 
#  first, in order ot track two indexs and the sum value, we need a package to 
# 	store them, tuple is a good choice and namedtuple provide a good access to 
# 	manipulate the tuple with our defined variables like start ,end,sum which gives
# 	us a intuiative feel.
# 	Secondly, since this problem is to find the continious maximum subarray, which simplified the 
# 	problem, and we can abandon the negative sum in the previous procee untill we find a 
#	positive value. the initial state is [a[0],0,0]. 


















