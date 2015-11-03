# Given two binary strings, return their sum (also a binary string).
# for example, a=11,b=1,return 100

class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):	
        # Write your code here
        if not a and not b:
        	return ''
        elif not a:
        	return b
        elif not b:
        	return a
        ##convert the string to decimal value
        # num_a=0
        # degree=1
        # for i in range(len(a)-1,-1,-1):
        # 	num_a+=degree*(int(a[i]))
        # 	degree*=2
        # num_b=0
        # degree=1
        # for j in range(len(b)-1,-1,-1):
        # 	num_b+=degree*(int(b[j]))
        # 	degree*=2s
        # return (num_a,num_b) 

        #using enumerate
        num_a=sum(int(c)*(2**i) for i,c in enumerate(a[::-1]) )
        num_b=sum(int(c)*(2**i) for i,c in enumerate(b[::-1]) )


        num = num_a + num_b
        result=[]
        while num/2 != 0:
        	result.append(str(num%2))
        	num/=2
        result.append(str(num)) #last bit of the result
        result=''.join(result[::-1])
        return result


#the method i use is to transfer the string to decimal value and finally transfer 
# 	the decimal value to the binary representation, one thing need to pay attention is that
# 	code line from 10 -15 to case which None and empty.



