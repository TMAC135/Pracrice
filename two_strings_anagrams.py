
"""

Write a method anagram(s,t) to decide if two strings are anagrams or not

example:
Given s="abcd", t="dcab", return true

challenge:
O(n) time, O(1) space

"""


class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        if not s and not t:
        	return True
        if not s or not t:
        	return False
        d={}
        for i in s:
        	if i not in d:
        		d[i]=1
        	else:
        		d[i]+=1
        for j in t:
        	if j not in d:
        		return False
        	else:
        		d[j]-=1
        		if d[j]<0:
        			return False
        return True