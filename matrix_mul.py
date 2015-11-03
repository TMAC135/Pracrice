## this is the python code for the matrix multiplication
#the two input are A(m*q) B(q*n) the output is C(m*n)
import numpy as np
def mul(A,B):
	if A == [] or B == []:
		return "there is null matrix,please input two other matrices again"
	row_A = len (A[:,])
	column_A = len (A[0,:]) #should be equal to row of B
	row_B = len (B[:,0])
	column_B = len (B[0,:])
	if column_A != row_B:
		return "dimention is not matching"
	C=np.zeros((row_A,column_B))
	for i in range(row_A):
		for j in range(column_B):
			sum = 0
			for ii in range(column_A):
				sum += A[i,ii] * B[ii,j]
			C[i,j] = sum
	return C

