"""
Given k strings, find the longest common prefix (LCP).

Example:
For strings "ABCD", "ABEF" and "ACEF", the LCP is "A"
For strings "ABCDEFG", "ABCEFG" and "ABCEFA", the LCP is "ABC"

"""

class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix

"""
Great example to use the list to do some operations on the strings, 
the thoughts are pretty simple since we compare the element which is popped
from the recent comparing string, and we will return the res once we find there 
exits a different value.

Notice that:
the first way i did: 
s=sorted(L,key=lambda x:x.pop(0)), which not the case we want.



"""
    def longestCommonPrefix(self, strs):
        # write your code here
        if not strs:
        	return ""
        L=[list(i) for i in strs]
        # return L
        res=[]
        while([] not in L):
        	cop=L[0].pop(0)
        	# return cop
	        for i in xrange(1,len(L)):
	        	tmp=L[i].pop(0)
	        	# return tmp
	        	if tmp!=cop:
	        		return ''.join(res)
	        res.append(cop)
        return ''.join(res)



if __name__=='__main__':
	print Solution().longestCommonPrefix(['ABCD','ABEF','ACEF'])