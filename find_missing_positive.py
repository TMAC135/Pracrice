#Given an unsorted integer array, find the first missing positive integer.
#Given [1,2,0] return 3, and [3,4,-1,1] return 2.


#My solution
class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # write your code here
        if not A:
        	return 1
        A.append(-1) #the reason why I append the '-1' to this list is that I am starting 
        			# passing the loop from A[1] instead of A[0], this may cause probelm 
        			#like the list [1,2,3,4,5]
        A.sort()
        val = 0
        for i in xrange(1,len(A)):
        	if A[i] > 0 and A[i] != A[i-1]:
        		val += 1
        		if A[i] != val:
        			return val
        return val+1

#solution from other which is pretty tricky 

# class Solution:
#     # @param A, a list of integers
#     # @return an integer
#     # @a very subtle solution
#     def firstMissingPositive(self, A):
#         n=len(A)
#         for i in range(n):
#             if A[i]<=0: A[i]=n+2
#         for i in range(n):
#             if abs(A[i])<=n:
#                 curr=abs(A[i])-1
#                 A[curr]=-abs(A[curr])
#         for i in range(n):
#             if A[i]>0: return i+1
#         return n+1
