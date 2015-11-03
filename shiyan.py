'''
class superlist(list):
	def _add_(self,b):
		return self.pop()+b.pop()
	def _sub_(self,b):
		a=self[:]
		b=b[:]
		return a.pop()-b.pop()'''

'''
def func(a):
	return a+2


if __name__ == '__main__':
	a=100
	print(func(a))
'''

# class num(object):
# 	# feather='this is string inside the class'
#    	def __init__(self, value):
#        	self.value = value
#     def getNeg(self):
#         return -self.value
#     def setNeg(self, value):
#         self.value = -value
#     def delNeg(self):
#         print("value also deleted")
#         del self.value
#     neg = property(getNeg, setNeg, delNeg, "I'm negative")

# if __name__ == '__main__':
# 	x = num(1.1)
# 	print(x.neg)
# 	x.neg = -22
# 	print(x.value)
# 	print(num.neg.__doc__)
# 	del x.neg

# class shiyan(object):
# 	def __init__(self):
# 		self.add=1
# 	def add1(self,res):
# 		res[1]=1

# 		# return res


# if __name__=='__main__':
# 	a=shiyan()
# 	res={}
# 	a.add1(res)
# 	for i in res:
# 		print res[i]


# Experiment about the attribute in class 

class Circle(object):
	__slots__=('name','age')
	def __init__(self,name,age,year):
		self.name=name
		self.age=age
		self.yaer=year
	def __getattr__(self,name):
		if name=='area':
			return 4
		elif name=='length':
			return 8
		else:
			object.__getattr__(self,name)
	def __setattr__(self,name,value):
		if name in ['area','length']:
			raise TypeError('not acceptable')
		object.__setattr__(self,name,value)

















