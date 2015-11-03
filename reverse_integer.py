# Reverse digits of an integer. Returns 0 when the reversed integer
# overflows (signed 32-bit integer).

# example: x=123, return 321,x=-123 return -321

# Bad version of the answer: using the list manipulation:
# class Solution:
#     # @param {int} n the integer to be reversed
#     # @return {int} the reversed integer
#     def reverseInteger(self, n):
#         # Write your code here 
#         array=list(str(abs(n)))
#         resu = ""
#         for i in range(len(array)-1,-1,-1):
#         	resu+=array[i]
#         return 0 if n==0 or int(resu)>2147483647 else (n/abs(n))*int(resu)

# if __name__ == '__main__':
# 	test = [1234,0,-3432,1534236469,-362547656725467235467]
# 	a=Solution()
# 	for i in test:
# 		print a.reverseInteger(i)
        	

#Notice: we need to eleminate the case where the reversed number is out of memory while the 
# 	original number is not, 
#The method above is not good since it need a lot of memory, and we need to get rid of this 
# 	problem.

# Better version: the total run time for the above two cases are almost the same
class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
    	if n == 0:
    		return 0
    	s=abs(n) #starting point of the loop
    	res=0
    	while not (s==0):
    		rem = s%10
    		s=s/10
    		res=10*res+rem
    	return 0 if  res>2147483647 else (n/abs(n))*res

if __name__ == '__main__':
	test = [1234,0,-3432,1534236469,-362547656725467235467]
	a=Solution()
	for i in test:
		print a.reverseInteger(i)
