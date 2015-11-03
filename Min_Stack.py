"""
Implement a stack with min() function, which will return the smallest number in the stack.

It should support push, pop and min operation all in O(1) cost.

Example: 
push(1)
pop()   // return 1
push(2)
push(3)
min()   // return 2
push(1)
min()   // return 1

Note:
min operation will never be called if there is no number in the stack.


"""


class MinStack(object):
"""
Basically, the main point of this problem is to use another stack to 
store the minimum information.
Notice that if we pop the value which it happens to be the minimum value of the 
current stack, thus we need a stack to store the minimum information.

"""


    def __init__(self):
        # do some intialize if necessary
        self.stack=[]
        self.minimum=[]

    def push(self, number):
        # write yout code here
        if not self.minimum:
            self.minimum.append(number)
        elif number<=self.minimum[-1]:
            self.minimum.append(number)
        self.stack.append(number)

    def pop(self):
        # pop and return the top item in stack
        tmp=self.stack[-1]
        if tmp==self.minimum[-1]:
            self.minimum.pop()
        return self.stack.pop()

    def min(self):
        # return the minimum number in stack
        return self.minimum[-1]





