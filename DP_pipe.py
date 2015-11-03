#the profit of the pipe 
# we are given the price of the related length:
# 	p=[1,5,8,9,10,17,17,20,24,30] corresponds to the length of 
	# [1,2,3,4,5,6,7,,8,9,10]

# bottom-up 
# class Solution(object):
# 	"""docstring for Solution"""
# 	def pipe1(self,p,length):
# 		r= [0 for _ in range(length+1)]
# 		s=[0 for _ in range(length+1)] #s is to record the location where we should cut
# 		if length == 0:
# 			return 0
# 		for i in range(1,length+1):
# 			q=0
# 			for j in range(1,i+1):
# 				# q=max(q,r[i-j]+p[j-1])
# 				if q<r[i-j]+p[j-1]: #if we want to track the position where we should cut 
# 					q=r[i-j]+p[j-1]
# 					s[i]=j
# 			r[i]=q
# 		return [r,s]


#top_down

class Solution(object):
	"""docstring for Solution"""
	def pipe2(self,p,length):
		r=[0 for _ in range(length+1)]
		s=[0 for _ in range(length+1)]
		self.solve(p,length,r,s)
		return [r,s]

	def solve(self,p,length,r,s):
		if length == 0 :
			return r[0]
		if r[length]>0:
			return r[length]

		q=0
		for i in range(1,length+1):
			# q=max(q,self.solve(p,length-i,r,s)+p[i-1])
			if q<self.solve(p,length-i,r,s)+p[i-1]:
				q=self.solve(p,length-i,r,s)+p[i-1]
				s[length]=i
		r[length]=q
		return r[length]

#Gnerally speaking, the topdown and bottom up method are similar,
# 	the key idea behind this is to get rid of the repeaded calculation, bottom up need 
# 	to construct the problem well so that you can use the inforamtion you had calculated
# 	before, and store the calculated information. Thr top down method are more difficult to
# 	to understand but it basically is recursion, once you find the way to store the knowm 
# 	information and how to recursively solve the problem, it is much easier.

