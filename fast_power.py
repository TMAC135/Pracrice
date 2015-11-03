"""
Calculate the an % b where a, b and n are all 32bit integers.

Example: 
For 231 % 3 = 2
For 1001000 % 1000 = 0

Challenge:
do it in O(logn)
"""

class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer

    the trick here is to use the euqation:
    (a * b) % p = (a % p * b % p) % p

    and also we need to distinguish the odd num and even number of n, 
    """
    def fastPower(self, a, b, n):
        # write your code here
		if n==1:
			return a%b
		if n==0:
			return 1%b
		tmp=self.fastPower(a,b,n/2)
		tmp=(tmp*tmp)%b
		if n%2==1:
			tmp=(tmp*a)%b
		return tmp