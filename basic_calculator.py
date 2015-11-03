# ##this is the first version I write, actually I don't consider the case where there are more than
# # 2 digit to represent the string.Actually,after seeing the code others write, the main difference
# #is the thought of how to save the number that is transfered from string to int, we need process the
# #multiplication and divide first.
#
# ##nput: the string like '1 + 2 *3'
# #output: the integer
#
#
# class Solution(object):
# 	def basic_cal(self,string):
# 		string_no_space=self.delete_space(string)
# 		length=len(string_no_space)
# 		for i in range(length):
# 			if string_no_space[i] == "*":
# 				string_no_space[i]=str(int(string_no_space[i-1]) * int(string_no_space[i+1]))
# 				string_no_space.remove(string_no_space[i-1])
# 				string_no_space.remove(string_no_space[i+1])
# 				string_no_space.append(" ")
# 			if string_no_space[i] == "/":
# 				string_no_space[i]=str(int(string_no_space[i-1]) / int(string_no_space[i+1]))
# 				string_no_space.remove(string_no_space[i-1])
# 				string_no_space.remove(string_no_space[i+1])
# 				string_no_space.append(" ")
# 		string_no_space=self.delete_space(string_no_space)
# 		length_new=len(string_no_space)
# 		for ii in range(length_new):
# 			if string_no_space[ii] == "+":
# 				string_no_space[ii]=str(int(string_no_space[ii-1]) + int(string_no_space[ii+1]))
# 				string_no_space.remove(string_no_space[ii-1])
# 				string_no_space.remove(string_no_space[ii+1])
# 				string_no_space.append(" ")
# 			if string_no_space[ii] == '-':
# 				string_no_space[ii]=str(int(string_no_space[ii-1]) - int(string_no_space[ii+1]))
# 				string_no_space.remove(string_no_space[ii-1])
# 				string_no_space.remove(string_no_space[ii+1])
# 				string_no_space.append(" ")
# 		string_no_space=self.delete_space(string_no_space)
# 		return int(string_no_space)
#
#
# ##the function we use for deleting the space in the string
# 	def delete_space(self,string):
# 		length=len(string)
# 		#collect the string without any spaces
# 		string_no_space=[]
# 		for i in range(length):
# 			if string[i]!= " ":
# 				string_no_space.append(string[i])
# 		return string_no_space

## the code below is written by others, the can handle the situation which contain the
#parethetheses() , the idea he use is to divide the string into operand and operator,
#the operand will only store the number (notice that we need to consider the case which
#transfer '11' as 11 ), the operator only store '+' '-' '*' '/' and '(' ')', the way to
#realize the priority of calculation is to have different cases for '+','-' and '*' '/'
#we only store the operand and operator when we meet '*' and '/', but once when we meet '+' and '-'
#we need to calculate all the multiplications or divisions before.
## Besides, this code split the calculation part from string manipulations. Basically, the
#operand and operator will yield the calculation easily.
    def calculate(self, s):
        operands, operators = [], []
        operand = ""
        for i in reversed(xrange(len(s))):
            if s[i].isdigit():
                operand += s[i]
                if i == 0  or not s[i-1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif s[i] == ')' or s[i] == '*' or s[i] == '/':
                operators.append(s[i])
            elif s[i] == '+' or s[i] == '-':
                while operators and \
                      (operators[-1] == '*' or operators[-1] == '/'):
                    self.compute(operands, operators)
                operators.append(s[i])
            elif s[i] == '(':
                while operators[-1] != ')':
                    self.compute(operands, operators)
                operators.pop()

        while operators:
            self.compute(operands, operators)

        return operands[-1]

    def compute(self, operands, operators):
        left, right = operands.pop(), operands.pop()
        op = operators.pop()
        if op == '+':
            operands.append(left + right)
        elif op == '-':
            operands.append(left - right)
        elif op == '*':
            operands.append(left * right)
        elif op == '/':
            operands.append(left / right)



