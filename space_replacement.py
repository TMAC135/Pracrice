##Write a method to replace all spaces in a string with %20.
 # The string is given in a characters array, 
 # you can assume it has enough space for replacement 
 # and you are given the true length of the string.

 #example: Given "Mr John Smith", length = 13.
 # The string after replacement should be "Mr%20John%20Smith".

class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        # Write your code here
        if not string:
        	return []
        array = list(string)
        for _ in xrange(length):
        	if array[0] != ' ':
        		array.append(array[0])
        	else:
        		array.append('%20')
        	array.remove(array[0])
        return array
        # str = ''.join(array)
        # return str

if __name__=='__main__':
    print Solution().replaceBlank('he eq  weq',10)

# import :
#when we do remove operation in list, the index will change after remove,
#	for example, a=[1,2,3,4],a.remove(1)=[2,3,4], now a[0] = 2 instead of a[1]=2;
#	it is extremely important when we do operation on the array when we have for i in range
#	(range),
# #        for _ in xrange(len(array)):
#         	if array[i] != ' ':
#         		array.append(array[i])
#         	else:
#         		array.append('%20')
#         	array.remove(array[i])

# class Solution(object):
#     """docstring for Solution"""
#     def replaceBlank(self,string,length):
#         array=list(string)

