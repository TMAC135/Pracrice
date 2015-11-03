class Solution(object):
	def strStr(self,source,target):
	   if source == None or target == None:
	       return -1
		if len(source) < len(target):
			return -1
		if len(target)==0:
			return 0
		i=0
		j=0
		while i < len(source):
			if source[i] == target[j]:
				j+=1
			i+=1
			if j >= len(target):
				return i-len(target)
		return -1