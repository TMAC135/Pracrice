"""
	strstr (a.k.a find sub string), is a useful function in string operation. Your task is to implement this function.
For a given source string and a target string, you should output the first index(from 0) of target string in source string.
If target does not exist in source, just return -1.

Example: 
If source = "source" and target = "target", return -1.
If source = "abcdabcdefg" and target = "bcd", return 1.

Challenge:
O(n2) is acceptable. Can you implement an O(n) algorithm? (hint: KMP)

Clarification
Do I need to implement KMP Algorithm in a real interview?

	Not necessary. When you meet this problem in a real interview, the interviewer may just want to 
test your basic implementation ability. But make sure your confirm with the interviewer first.


"""
class Solution:
    def strStr(self, source, target):
    	"""
    	notice that for this case, target = None and target = '' are 
    	different cases,we can't deal with that in 
    	if not target:
    		
    	"""
        # write your code here
        # if not source and not target:
        # 	return 0
        # if not target:
        # 	return 0
        # if not source:
        # 	return -1
        if target==None:
        	return -1
        if target=='':
        	return 0
        if not source:
        	return -1

        for i in xrange(len(source)):
        	if self.isvalid(source[i:],target):
        		return i
        return -1

    def isvalid(self,s,t):
    	if len(s)<len(t):
    		return False
    	for i in xrange(len(t)):
    		if s[i]!=t[i]:
    			return False
    	return True

