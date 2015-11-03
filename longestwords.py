# Given a dictionary, find all of the longest words in the dictionary.
# input: a list of strings
# output: a list of strings
class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        # write your code here
        # if dictionary == "" or dictionary == None:
        # 	return dictionary
        if not dictionary:
        	return dictionary
        longest = [] #this varable is used to return the final list 
        word_length = 0 #this value is used to capture the length of the word
        for i in xrange(len(dictionary)):   # comparing with other's code, we can process 
        	if len(dictionary[i]) > word_length: # the word directly
        		longest = []
        		word_length = len(dictionary[i])
        		longest.append(dictionary[i])
        	elif len(dictionary[i]) == word_length:
        		longest.append(dictionary[i])
        return longest

##code from other

# class Solution:
#     def longestWords(self, dictionary):
#         """
#         :param dictionary: a list of strings
#         :return: a list of strings
#         """
#         ret = []
#         for word in dictionary:
#             if not ret or len(word) > len(ret[0]):
#                 ret = [word]

#             elif len(word) == len(ret[0]):
#                 ret.append(word)

#         return ret