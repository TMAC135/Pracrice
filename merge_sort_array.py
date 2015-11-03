# Given two sorted integer arrays A and B, merge B into A as one sorted array.
# A = [1, 2, 3, empty, empty], B = [4, 5]
# After merge, A will be filled as [1, 2, 3, 4, 5]

class Solution:
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
# option 1: not in place, thus we use extral space which is O(m+n)
    def mergeSortedArray(self, A, m, B, n):
        tmp = [0 for i in range(m + n)]
        i = 0; j = 0; k = 0
        while i < m and j < n:
            if A[i] <= B[j]:
                tmp[k] = A[i]
                i += 1
            else:
                tmp[k] = B[j]
                j += 1
            k += 1
        if i == m:
            while k < m + n:
                tmp[k] = B[j]
                k += 1
                j += 1
        else:
            while k < m + n:
                tmp[k] = A[i]
                i += 1
                k += 1
        for i in range(0, m + n):
            A[i] = tmp[i]
# option 2: in place merge sort:
    # def mergeSortedArray(self, A,m, B,n):
    #     # write your code here
    #     last=m+n-1
    #     m=m-1
    #     n=n-1
    #     while m>=0 and n>=0:
    #     	if A[m]>B[n]:
    #     		A[last]=A[m]
    #     		m=m-1
    #     	else:
    #     		A[last]=B[n]
    #     		n=n-1
    #     	last=last-1
    #     while n>=0:
    #     	A[n]=B[n]
    #     	n=n-1



 # This is just the test case for we debug, we must return the final sorted array
    # since the array in the function will be destroyed when we get out of the function.
    # This is the same phenomenon for the stack, LIFO 
#     def mergeSortedArray(self, A,m, B,n):
#         # write your code here
#         last=m+n-1
#         m=m-1
#         n=n-1
#         while m>=0 and n>=0:
#         	if A[m]>B[n]:
#         		A[last]=A[m]
#         		m=m-1
#         	else:
#         		A[last]=B[n]
#         		n=n-1
#         	last=last-1
#         while n>=0:
#         	A[n]=B[n]
#         	n=n-1
#         return A
# if __name__ == '__main__':
# 	a=Solution()
# 	test=[[1,2,3,0,0],3,[1.1,2.2],2]
# 	for i in a.mergeSortedArray(test[0],test[1],test[2],test[3]):
# 		print i


