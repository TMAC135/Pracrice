# matrix chain order

# we are given the dimention of Ai in multiplication,
# 	say A1A2...Ai...An, the list p contains all the dimention information:
# 	p=[p0,p1,...,pn], the dimention of the final result is p0*pn, in fact, A1:p0*p1, A2: p1*p2
# 	A3:p2*p3,..An:pn-1*pn
#	for example: p =[10,20,50,1,100], the num of multiplications Ai*Aj=p(i-1)*p(k)*p(j)

class Solution(object):
	def matrix_chain(self,m,p,s):
		for delta in range(1,len(p)-1):
			for i in range(len(p)-delta-1):
				j=i+delta
				m[i][j]=999999999999
				for k in range(i,j):
					tmp = m[i][k]+m[k+1][j]+p[i]*p[k+1]*p[j+1]
					if tmp < m[i][j]:
						m[i][j]=tmp
						s[i][j]=k

		return m

# notice the index of the array ,be careful when we use the range()

# now given the s[i][j] information which gives us the optimal position 
# 	of partition, we can recursively plot the parenthesis,similarlly, the 
# 	base case is when plot the single matrix, otherwise we will partition AiA(i+1)...Aj
# 	to (Ai...Ak)(Ak+1Aj)
	def parenthesis(self,s,i,j):
		if i == j:
			print 'A'+str(i),
		else:
			print '(',
			self.parenthesis(s,i,s[i][j])
			self.parenthesis(s,s[i][j]+1,j)
			print ')',

