# Merge two given sorted integer array A and B into a new sorted integer array.

# chanllege:
# How can you optimize your algorithm if one array is very large and the other is very small?

# comparing with the previous problem, we need to return the array, one way is to use extra space 
#   tmp to pass A and B, but to solve the chanllege, we can choose the shorter array and insert it 
#   into hte longer array
class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        if not A:
            return B
        elif not B:
            return A
        m=len(A)
        n=len(B)
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
        return tmp
        