# coding=utf-8

"""
Write a function that add two numbers A and B. You should not use + or any arithmetic operators

Example
Given a=1 and b=2 return 3

Note
There is no need to read data from standard input stream. Both parameters are given in function aplusb, you job is to calculate the sum and return it.

Challenge
Of course you can just return a + b to get accepted. But Can you challenge not do it like that?


Clarification
Are a and b both 32-bit integers?
Yes.

Can I use bit operation?
Sure you can.

"""

class Solution:
    """
    @param a: The first integer
    @param b: The second integer
    @return:  The sum of a and b

    I am alomost there, i have come out the way
    (a^b) + (a&b)<<1, 
    actually there is another add in the equation, all we need to do is 
    to do the process again untill the carry is 0

    """
    def aplusb(self, a, b):
        # write your code here, try to do it without arithmetic operators.
        while b:
        	carry=a&b
        	a=a^b
        	b=carry<<1

        return a



if __name__ == '__main__':
	print Solution().aplusb(2,100)

