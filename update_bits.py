"""
Given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to set all bits between i and j in N equal to M 
(e g , M becomes a substring of N located at i and starting at j)

Example
Given N=(10000000000)2, M=(10101)2, i=2, j=6
return N=(10001010100)2

Note
In the function, the numbers N and M will given in decimal, you should also return a decimal number.

Challenge
Minimum number of operations?

Clarification
You can assume that the bits j through i have enough space to fit all of M. That is, if M=10011， you can assume that
 there are at least 5 bits between j and i. You would not, for example, have j=3 and i=2, because M could not fully fit between bit 3 and bit 2.

"""

class Solution:
    #@param n, m: Two integer
    #@param i, j: Two bit positions
    #return: An integer
    """
    Steps:
	(e.g. n = (100,0000,0000)2, m = (1,0101)2, i = 2, j = 6)

	Method1:
	(1<<j+1) - (1<<i) : 0000,0000,0000,0000,0000,0000,0111,1100
	~((1<<j+1) - (1<<i)) : 1111,1111,1111,1111,1111,1111,1000,0011
	n & ~((1<<j+1) - (1<<i)) : 0000,0000,0000,0000,0000,0100,0000,0000
	m<<i : 101,0100
	n & ~((1<<j+1) - (1<<i)) | m<<i : 0000,0000,0000,0000,0000,0100,0101,0100

	if j == 31, we should reconsider the case to avoid the overflow.
    """
    def updateBits(self, n, m, i, j):
        # write your code here

        # dinn't pass with python
        return ~((1<<j+1)-(1<<i)) & n | m<<i if j!=31 else \
        		~((0xffffffff)-(1<<i)) & n | m<<i

        #  pass version with C++
        return n & ~((j == 31 ? 0xffffffff : (1<<j+1)-1) - (1<<i)+1) | m<<i;
