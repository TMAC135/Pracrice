
#coding=utf-8

"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Clarification

What constitutes a word?
A sequence of non-space characters constitutes a word.

Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.

How about multiple spaces between two words?
Reduce them to a single space in the reversed string.

"""


class Solution:
    # @param s : A string
    # @return : A string
    """
    Be careful about consider all the cases
    'were' ,'   ','  v  ',

    """

    def reverseWords(self, s):
        # write your code here
        if not s:
        	return ''
        res=''
        # strip all the space in the head and tail
        for head in xrange(len(s)):
        	if s[head] != ' ':
        		break

        for tail in xrange(len(s)-1,-1,-1):
        	if s[tail] != ' ':
        		break
       	# if head is greater than tail, which means all the strings are space
       	# if head==tail, which means we only have one string in this string.
        if head >= tail:
        	return s[head]

        res=''
        # word is the 
        word=''
        for i in xrange(tail,head-1,-1):
        	if s[i] != ' ':
        		word += s[i]
        	else:
        		res += word[::-1] 
        		word = ''
        		# this is to judge if the previous element is space
        		if res[-1] != ' ':
        			res += ' '
        return res+word[::-1]


if __name__ == '__main__':
	print Solution().reverseWords('wore')
	print Solution().reverseWords('    ')
	print Solution().reverseWords('  b   ')
	print Solution().reverseWords(' i am not')




