# Given a roman numeral, convert it to an integer.
# The answer is guaranteed to be within the range from 1 to 3999.

# Example: IV - 4, XII - 12, XCIX - 99


# symbols: I:1,V:5,X:10,L:50,C:100,D:500,M:1000
class Solution:
    # @param {string} s Roman representation
    # @return {int} an integer
    def romanToInt(self, s):
        # Write your code here
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        if not s:
        	return 0
        result=0
        prev=0
        for i in xrange(len(s)-1,-1,-1):
        	value=d[s[i]]
        	if value>=prev:
        		result+=value
        		prev=value
        	else:
        		result-=value
        return result

if __name__=='__main__':
	a=Solution()
	test=['IV','XII','XXI','XCIX']
	for i in test:
		print a.romanToInt(i)

