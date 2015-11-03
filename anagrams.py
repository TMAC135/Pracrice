"""
Given an array of strings, return all groups of strings that are anagrams.

Example:
Given ["lint", "intl", "inlt", "code"], return ["lint", "inlt", "intl"].
Given ["ab", "ba", "cd", "dc", "e"], return ["ab", "ba", "cd", "dc"].



"""
# first version of the my solution but didn't work
# class Solution:
# 	# @param strs: A list of strings
# 	# @return: A list of strings
# 	def anagrams(self, strs):
# 		# write your code here
# 		if not strs:
# 			return []
# 		d={}
# 		for i in strs:
# 			if len(i) not in d:
# 				d[len(i)]=[i]
# 			else:
# 				d[len(i)].append(i)
# 		# return d
# 		res=[]
# 		for i in (d.keys()):
# 			l1=len(res)
# 			com=d[i]
# 			while (com):
# 				tmp=com.pop()
# 				for j in com:
# 					if self.isanagram(tmp,j):
# 						res.append(j)
# 			if len(res)>l1:

							  
# 		return res



# 	def isanagram(self, s, t):
# 		# write your code here
# 		d={}
# 		if not t:
# 			return False
# 		for i in s:
# 			if i not in d:
# 				d[i]=1
# 			else:
# 				d[i]+=1
# 		for j in t:
# 			if j not in d:
# 				return False
# 			else:
# 				d[j]-=1
# 				if d[j]<0:
# 					return False
# 		return True


"""
this is the method from others, notice that for python, we can use
the sorted function to sort the strings, thus using this method, if two 
strings are anagrams,the sorted strings of these 2 must be the same,this 
is the key of this method.

"""
class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        dict = {}
        for word in strs:
            sortedword = ''.join(sorted(word))
            dict[sortedword] = [word] if sortedword not in dict else dict[sortedword] + [word]
        res = []
        for item in dict:
            if len(dict[item]) >= 2:
                res += dict[item]
        return res



if __name__=='__main__':
	# print Solution().anagrams(["tea","and","ate","eat","den"])
		print Solution().anagrams(['',''])












