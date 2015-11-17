# coding=utf-8

"""
Implement an algorithm to determine if a string has all unique characters
Example
Given "abc", return true.

Given "aab", return false.

Challenge
What if you can not use additional data structures?
"""

class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, str):
        # write your code here
        """
        try to solve it without any data structures like list, dictionaries,but not working

        if not str:
            return True
        cur=255
        for i in xrange(len(str)):
            if self.ischaracter(str[i]):
                if cur & ~ord(str[i]) == 0:
                    return False
                else:
                    cur = cur & ord(str[i])
                    # return chr(cur)
        return True
        
    def ischaracter(self,i):
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
            return True
        else:
            return False

         """
        """
        不需要判断是否是字母，character 包括其他字符！！！！！
        """
        if not str:
        	return True
        d=[]
        for i in str:
         	if self.ischaracter(i):
         		if i not in d:
         			d.append(i)
         		else:
         			return False
        return True

    def ischaracter(self,i):
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
            return True
        else:
            return False


if __name__ == '__main__':
	print Solution().isUnique('abc__c')