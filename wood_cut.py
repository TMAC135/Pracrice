"""
Given n pieces of wood with length L[i] (integer array). Cut them 
into small pieces to guarantee you could have equal or more than 
k pieces with the same length. What is the longest length you can get
from the n pieces of wood? Given L & k, return the maximum length of the small pieces

Example
For L=[232, 124, 456], k=7, return 114.

Note
You couldn't cut wood into float length.

Challenge
O(n log Len), where Len is the longest length of the wood.

"""

class Solution:
	"""
	@param L: Given n pieces of wood with length L[i]
	@param k: An integer
	return: The maximum length of the small pieces.

	The key idea behind binary search is to how to anaylyze the 
	final answer of the elements, like we end up with getting 2 elements or 
	1 element finally, and another important thing we need to focus on is that 
	the equal sign of the comparison, this is highly related to the different process.


	"""
	def woodCut(self, L, k):
		# write your code here
		if not L:
			return 0
		# L.sort()
		ss=1
		ee=max(L)
		while ss<ee-1:
			mm=(ss+ee)/2
			count=self.count_len(L,mm)
			if count<k:
				ee=mm
			else:
				ss=mm
		# we end up with getting two nodes finally, but there are still some
		# uncertainty about these 2 nodes and needed to be examined. 
		count1=self.count_len(L,ss)
		count2=self.count_len(L,ee)
		if count1<k:
			return 0 #which means we don't any solution for this k 
		elif count2>=k:
			return ee # this is the case which we keep keep push left node to the left and thus 
					# we didn't check the right node of the binary search.
		else:
			return ss


	def count_len(self,L,s):
		count=0
		for i in L:
			count+=i/s
		return count

# Solution 2:same idea as me but it use list comprehension which is 
# more like a python code

class Solution2(object):

    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        if sum(L) < k:
            return 0
            
        maxLen = max(L)
        start, end = 1, maxLen
        while start + 1 < end:
            mid = (start + end) / 2
            # use method sum and list comprehension 
            pieces = sum([l / mid for l in L])
            if pieces >= k:
                start = mid
            else:
                end = mid
                
        if sum([l / end for l in L]) >= k:
            return end
        return start



if __name__=='__main__':
	print Solution2().woodCut([232,124,456],7)


