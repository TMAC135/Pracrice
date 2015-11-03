class Solution (object):
	def twosum(self,list,target):
		length = len (list)
		if length < 2:
			return 'please give us a new list with more than two values'
		true = 0
		for i in range (length-1):
			for j in range (i+1,length):
				if list [i] + list [j] == target :
					true == 1
					index1=i+1
					index2=j+1
					break
			else:
				continue
			break
		if true == 1 :
			return (index1,index2)
		else:
			return 'no such two values which give us target sum'

