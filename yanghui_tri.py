# coding=utf-8

"""
construct the yanghui triangular using queue
"""

class yanghui(object):
	"""docstring for yanghui"""
	def Queue(self,level):
		if level == 1:
			return [[1]]
		elif level == 2:
			return [[1],[1,1]]
		res = [[1],[1,1]]
		for _ in xrange(3,level+1):
			prev = res[-1]
			i = 0
			tmp = []
			while(i + 1 < len(prev)):
				tmp.append(prev[i] + prev[i+1])
				i += 1
			res.append([1]+tmp+[1])
		return res

	def printout(self,queue):
		length = len(queue)
		max_length = 2*length - 1
		for i in xrange(1,length + 1):
			space = ' '*((max_length -2*i + 1)/2+1)
			string = ''
			for ii in queue[i-1]:
				string += str(ii) + ' ' 
			print space + string


if __name__ == '__main__':
	res=yanghui().Queue(10)
	yanghui().printout(res)


