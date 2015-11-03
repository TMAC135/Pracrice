# Given a array, find the maximum length of nondecreasing subarray
# 	this subarray don't need to be continuous. 
# Basically, this can be interpreted as the insertion problem, we treat this as the dynamaic 
# problem, we store the information for the previous n-1 data(d[1...n-1]), then the next the point is 
# to find the recuision relation between the d[n] and the previous inforamtion, now the trick part is 
# how to represent the previous information in the way we can track. Usually, matrix and array are 
# the most common ways.
#	The method here doesn't gives us the final array, since it only hold the last digit of the 
#maximum subarray, we ignore the inforamtion in between. 
# exec 'shiyan=11'

class LIS(object):
	"""docstring for LIS"""

	def l_i_s(self,A):
		if not A:
			return 0
		B=[A[0]]
		length=1
		for i in range(1,len(A)):
			pos=self.Insertion(B,A[i])
			if pos == len(B):
				length+=1
				B.append(A[i])
			else:
				B[pos]=A[i]

		return (length,B)

	def Insertion(self,B,value):
		start=0
		end=len(B)-1
		mid=(start+end)/2
		if B[end]<= value:
			return end+1
		# method from others,
		while start < end:  #this is related to the base case, 
		# we want to find the maximum index that is greater to equal to value,but also the next index 
		# must be strictly less than this value,then we will construct the subproblem 
		# which is the same contion for the whole problem.
		# the base case is when there are two values, we check the condition.
			if B[mid] <= value:
				start = mid +1
			else:
				end = mid
			mid = (start + end)/2
		# if B[start] == value or B[end]== value:
		# 	pass
		# elif B[end] < value:
		# 	B.append(value
		# elif B[start]> value:
		# 	B[start] = value
		# if B[end] < value:
		# 	B.append(value)
		# elif B[start] > value:
		# 	B[start] = value
		return start
if __name__ == '__main__':
	C=[1]
	value = [5]
	a=LIS()
	for i in value:
		print a.Insertion(C,i)


