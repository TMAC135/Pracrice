#coding=utf-8

"""
Given a string and an offset, rotate string by offset. (rotate from left to right)

Example
Given "abcdefg".

offset=0 => "abcdefg"
offset=1 => "gabcdef"
offset=2 => "fgabcde"
offset=3 => "efgabcd"

Challenge
Rotate in-place with O(1) extra memory

"""

class Solution:
    # @param s: a list of char
    # @param offset: an integer 
    # @return: nothing
    def rotateString(self, s, offset):
	    # write you code here

	    """
	    理解错题意了，要in place 旋转，因此不能pop最后的元素再粘在前面

	    """
	    # # using list. but not in place
	    # # if s:
	    # # 	list_str = list(s)
	    # # 	for _ in xrange(offset):
	    # # 		tmp=list_str.pop()
	    # # 		list_str=[tmp] + list_str
	    # # 	s=''.join(list_str)

	    # # operate in place 
	    # if s:
	    # 	for _ in xrange(offset):
	    # 		s=s[-1]+s
	    # 		s=s[:len(s)-1]
	    # return s

	    """
	    正确做法，应该再原址进行旋转：
	    以S="abcdefg"  offset=4为例子

		首先将字符串看做："abc"+"defg"

		先整体反转：得到 "gfed" + "cba"

		然后各自反转：得到“defg” + "abc" = "defgabc"



	    """

class Solution:
    # @param s: a list of char
    # @param offset: an integer 
    # @return: nothing
    def rotateString(self, s, offset):
        # write you code here
        if s!=None and len(s)!=0:
            left = 0
            right = len(s) - 1
            offset = offset%(right+1)
            self.rotateStr(s,0,right - offset)
            self.rotateStr(s,right - offset + 1,right)
            self.rotateStr(s,0,right)
        
        
    def rotateStr(self,s,left,right):
        while left<right:
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            left += 1
            right -= 1

