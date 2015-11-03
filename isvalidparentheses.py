##Given a string containing just the characters '(', ')', 
#'{', '}', '[' and ']', determine if the input string is valid.
#Example
#The brackets must close in the correct order, 
#"()" and "()[]{}" are all valid but "(]" and "([)]" are not.

#my solution
# class Solution:
#     # @param {string} s A string
#     # @return {boolean} whether the string is a valid parentheses
#     def isValidParentheses(self, s):
#         # Write your code here
#         if not s:
#         	return False
#         paren = 0
#         bra = 0
#         cur = 0
#         for i in xrange(len(s)):
#         	if paren == 1:
#         		if s[i] is not ")":
# 					return False
# 				else:

# 					paren = 0 
#         	elif bra == 1:
#         		if s[i] is not "]":
# 					return False
# 				else:
# 					bra = 0
#         	elif cur == 1:
#         		if s[i] is not "}":
# 					return False
# 				else:
# 					cur = 0

#         	if s[i] == "(":
#         		paren = 1
#         	elif s[i] == "[":
#         		bra = 1
#         	elif s[i] == "{":
#         		cur = 1	
#         return True


##clearly my first solution is not working, actually i don't know how to deal with the case which is 
# "{[()]}", this is where the stack uses , LIFO, 
# 解题思路：判断括号匹配的合法性。使用一个栈来解决问题。遇到左括号入栈，
# 遇到右括号，检查栈顶的左括号是否匹配，如果匹配，弹栈，如果不匹配，返回错误。
# 如果栈为空，而遇到右括号，同样返回错误。遍历完后，栈如果不空，同样返回错误。

# solution from other: it ignore the case where the s is none
class Solution:	
    # @return a boolean
    def isValidParentheses(self, s):
    	if not s:
    		return False
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            if s[i] == ')':
                if stack == [] or stack.pop() != '(':
                    return False
            if s[i] == ']':
                if stack == [] or stack.pop() != '[':
                    return False
            if s[i] == '}':
                if stack == [] or stack.pop() != '{':
                    return False
        if stack:
            return False
        else:
            return True











