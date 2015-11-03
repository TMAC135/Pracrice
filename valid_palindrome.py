# Given a string, determine if it is a palindrome, 
# considering only alphanumeric characters and ignoring cases.

# Example:	"A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        # Write your code here
        if not s:
        	return True
        head=0
        end=len(s)-1
        while(head<end):
        	if self.isalphanum(s[head]) and self.isalphanum(s[end]):
        		if ord(s[head])==ord(s[end]) or abs(ord(s[head])-ord(s[end]))==32:
        			head+=1
        			end-=1
        			continue
        		else:
        			return False
        	if not self.isalphanum(s[head]):
        		head+=1
        	if not self.isalphanum(s[end]):
        		end-=1
        return True

#Bool return,to judge whether the character is alpha or number      
    def isalphanum(self,c):
    	return True if (ord(c)>=48 and ord(c)<=57) or (ord(c)>=65 and ord(c)<=90) or \
    	(ord(c)>=97 and ord(c)<=122) else False
if __name__=='__main__':
	a=Solution()
	test=['A man a plan a CANAL : pANAMA   ,','RACE a car','','asa']
	for i in test:
		print a.isPalindrome(i)