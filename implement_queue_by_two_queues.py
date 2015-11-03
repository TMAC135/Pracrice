# The queue should support push(element), pop() and top() where
 # pop is pop the first(a.k.a front) element in the queue.


# challenge: implement it by two stacks, do not use any other data structure and push, pop and top should be O(1) by AVERAGE.

# this is my first idea that using one stack, since we can
# use the remove of the list to help us pop in the queue.
# 
# class Solution(object):
# 	"""
# 		this is my first idea that using one stack, since we can
# 	 use the remove of the list to help us pop in the queue.But it doesn't 
# 	 satisfy the problem.

# 	"""


# 	def __init__(self):
# 		self.stack1=[]
# 		self.stack2=[]

# 	def top(self):
# 	# write your code here
# 	# return the top element
# 		return self.stack1[0] if self.stack1 else None

# 	def push(self, element):
# 		# write your code here
# 		self.stack1.append(element)

# 	def pop(self):
# 		# write your code here
# 		# pop and return the top element
# 		tmp=self.top()
# 		if tmp:
# 			self.stack1.remove(self.stack1[0])
# 		return tmp



class Queue:
	"""
	basically we use two stacks, one is push_in stack,another
	is pop_out stack, then combining the two stacks, it just 
	acts like the Queue.
	"""


	def __init__(self):
		self.stack1=[]
		self.stack2=[]

	def top(self):
	# write your code here
	# return the top element
		if not self.stack2:
			while self.stack1:
				self.stack2.append(self.stack1.pop())
		return self.stack2[-1]


	def push(self, element):
		# write your code here
		self.stack1.append(element)

	def pop(self):
		# write your code here
		# pop and return the top element
		if not self.stack2:
			while self.stack1:
				self.stack2.append(self.stack1.pop())
		return self.stack2.pop()	


if __name__=='__main__':
	a=Solution()






