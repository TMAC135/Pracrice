#coding=utf-8


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

# class Circle(object):
# 	__slots__=('name','age')
# 	def __init__(self,name,age,year):
# 		self.name=name
# 		self.age=age
# 		self.yaer=year
# 	def __getattr__(self,name):
# 		if name=='area':
# 			return 4
# 		elif name=='length':
# 			return 8
# 		else:
# 			object.__getattr__(self,name)
# 	def __setattr__(self,name,value):
# 		if name in ['area','length']:
# 			raise TypeError('not acceptable')
# 		object.__setattr__(self,name,value)


# experiment of the generator, permutation generator

# def permutations(li):

# 	if len(li)==0:
# 		yield li
# 	else:
# 		for i in range(len(li)):
# 			li[0],li[i]=li[i],li[0]
# 			for item in permutations(li[1:]):
# 				yield [li[0]]+item


# if __name__=='__main__':
# 	for item in permutations(range(5)):
# 		print item


# experiment of the private attribute of the instance

# class A(object):
# 	"""docstring for A"""
# 	def __init__(self, arg):
# 		super(A, self).__init__()
# 		self.__name= arg

# 	def inf(self):
# 		print('private value is',self.__name)


# a=A(3)
# a.inf() #('private value is', 3)
# a.__name=2
# a.inf() #('private value is', 3)
# print('out of the class:',a.__name) #('out of the class:', 2)
# print a.__dict__ #{'__name': 2, '_A__name': 3},注意 _A__names属性
# print A.__dict__


# experiment of the descriptor,set the __init__, __set__,
# __get__,__delete__

class Nonneg(object):
	"""
	descriptor, nonnegtive
	"""
	def __init__(self,default=0):
		self.num = default

	def __get__(self,instance,owner):
		return self.num

	def __set__(self,instance,val):
		if val >= 0 :
			self.num = val
		else:
			print 'only valid for non negative number'

	def __delete__(self,instance):
		print 'can not delete this number'


class Movie(object):
	"""docstring for Movie"""
	rating=Nonneg()
	score=Nonneg()
	def __init__(self, arg):
		super(Movie, self).__init__()
		self.arg = arg


a=Movie(2)
a.rating=-1
a.score=5
del a.score
		







