# Write an algorithm which computes the number of trailing zeros in n factorial.

# Example: 11! = 39916800, so that would be 2

class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        result = 0 
        while (n):
            result += (n/5)
            n/=5
        return result

# 	Since 10 = 2*5 ,2 is always sufficient, thus we need to count the number of 
# 5, notice 25 = 5*5,contains 2 5's, then we recurcively divide 5 and count the number.