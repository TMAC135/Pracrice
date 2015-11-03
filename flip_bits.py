# Determine the number of bits required to flip if you want to
 # convert integer n to integer m.
 # example: given n =31(1111),m=14(01110),return 2

# Both n and m are 32-bit integers.

#first version of my solution, it can only solve the problem with positive a and b
# class Solution:
#     """
#     @param a, b: Two integer
#     return: An integer
#     """
#     def bitSwapRequired(self, a, b):
#         # write your code here
#         #first turn the a , b into binary representation
#         a_bin=self.changetype(a)
#         b_bin=self.changetype(b)
#         # make the length of string of a and b are the same size
#         if len(a_bin)<=len(b_bin):
#         	a_bin='0'*(len(b_bin)-len(a_bin))+a_bin
#         else:
#         	b_bin='0'*(len(a_bin)-len(b_bin))+b_bin
#         count =0
#         for i,j in zip(a_bin,b_bin):
#         	count+=(i!=j)
#         return count

#     # given the integer value, return the binary representation in string
#     def changetype(self,value):
#     	return bin(value)[2:]
# if __name__=='__main__':
# 	a=Solution()
# 	test = [31,32]
# 	print a.bitSwapRequired(test[0],test[1])

# this version is almost the same as previous one but I change the changetype function
# 	to contain the negative case. 
#  Python can generate the 2's representation for any length of the size, like 32bit,64 bit,
#by bin(value & 0xffff)

class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """
    def bitSwapRequired(self, a, b):
        # write your code here
        #first turn the a , b into binary representation
        a_bin=self.changetype(a)
        b_bin=self.changetype(b)
        # make the length of string of a and b are the same size
        if len(a_bin)<=len(b_bin):
        	a_bin='0'*(len(b_bin)-len(a_bin))+a_bin
        else:
        	b_bin='0'*(len(a_bin)-len(b_bin))+b_bin
        count =0
        for i,j in zip(a_bin,b_bin):
        	count+=(i!=j)
        return count

    # given the integer value, return the binary representation in string
    def changetype(self,value):

    	return bin(value)[2:] if value>0 else bin(value & 0xffffffff)[2:]




