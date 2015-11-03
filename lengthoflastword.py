#Given a string s consists of upper/lower-case alphabets 
# and empty space characters ' ', return the length of last word in the string.
# Example
#Given s = "Hello World", return 5


#my solution:
#first we need to count the space character in the last part of the 
#	string, then all we need to do is to scan the rest character and stop scaning
# 	when we encounter a space character
#	if the string are all space, we need to return 0
# class Solution:
#     # @param {string} s A string
#     # @return {int} the length of last word
#     def lengthOfLastWord(self, s):
#         # Write your code here
#         if not s:
#         	return 0
#         space = 0
#         for j in range(-1,-len(s)-1,-1):
#         	if s[j] == ' ':
#         		space+=1
#         	else:
#         		break
#         if space==len(s):
#         	return 0
#         count = 0 
#         for i in range(-space-1,-len(s)-1,-1):
#         	if s[i]==' ':
#         		break
#         	else:
#         		count+=1
#         return count


#solution from others, python is so powerful at string manipulations
#Another thing I need to improve is that try to combine related code into the 
#	simple code form, for example:
#	if something:
	# 	return l1
	# else:
	# 	return l2
# =>
# return l1 if something else l2

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        return len(s.split()[len(s.split())-1]) if s.split() != [] else 0




