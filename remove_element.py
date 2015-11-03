"""
	Given an array and a value, remove all occurrences of that value in place and return the new length.
The order of elements can be changed, and the elements after the new length don't matter.

Example:
Given an array [0,4,4,0,0,2,4,4], value=4
return 4 and front four elements of the array is [0,0,0,2]
"""


class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        if not A:
        	return 0
        setA=set(A)
        if elem not in setA:
        	return len(A)
        # here i sort the A first and then find the index of element
        # sorting the A will be O(nlogn), if we want to reduce the time
        # complexity, we can use dictionary to store the information.
        A.sort()
        index1=A.index(elem)
        index2=len(A)-A[::-1].index(elem)-1
        A[index1:(index2+1)]=[]
        # i=0
        # # version without remove elements from original array
        # for j in xrange(index,len(A)):
        # 	if A[j]==A[index]:

        # 		i+=1
        # 	else:
        # 		break
        # with remove from the original array
        # rep=0
        # j=index
        # while(j<len(A)):
        # 	if A[j]==A[index]:
        # 		A.remove(A[j])
        # 		rep+=1
        # 	else:
        # 		break

        return len(A)

if __name__=='__main__':
	print Solution().removeElement([0,4,4,0,0,2,4,4],4)