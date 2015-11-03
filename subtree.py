"""
 	You have two every large binary trees: T1, with millions of nodes,
 and T2, with hundreds of nodes. Create an algorithm to decide if 
 T2 is a subtree of T1.

 Example: T2 is a subtree of T1 in the following case:
      1                3
      / \              / 
T1 = 2   3      T2 =  4
        /
       4
T2 isn't a subtree of T1 in the following case:
      1               3
      / \               \
T1 = 2   3       T2 =    4
        /
       4

"""


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    # def isSubtree(self, T1, T2):
    #     # write your code here
    #     if not T2:
    #     	return True
    #     if not T1:
    #     	return False
    #    	# pre-order traversal of the two trees
    #     stack1=[T1]
    #     r1=[]
    #     while stack1:
    #         tmp=stack1.pop()
    #         r1.append(tmp.val)
    #         if tmp.right:
    #             stack1.append(tmp.right)
    #         if tmp.left:
    #         	stack1.append(tmp.left)
    #     stack2=[T2]
    #     r2=[]
    #     while stack2:
    #         tmp=stack2.pop()
    #         r2.append(tmp.val)
    #         if tmp.right:
    #             stack2.append(tmp.right)
    #         if tmp.left:
    #         	stack2.append(tmp.left)
    #      # just compare the r1 and r2, however this is satisfy the defination
    #      # subtree, notice that 
    #     if len(r1)<len(r2):
    #     	return False
    #     else:
    #     	for i in xrange(len(r1)):
    #     		if r1[i]==r2[0]:
    #     			if r1[i:]==r2:
    #     				return True
    #     return False
"""
still, I am not familiar with the recursion tricks, we need to be
causious about the basic case of the recursion.

"""


    def isSubtree(self, T1, T2):
        # write your code here
        if not T2  and T1:
        	return True
        if not T2:
        	return True
        if not T1:
        	return False
        if self.isidentical(T1,T2):
        	return True
        return self.isSubtree(T1.left,T2) or self.isSubtree(T1.right,T2)



    def isidentical(self,T1,T2):
    	if not T1 and not T2:
    		return True
    	if not T1 or not T2:
    	    return False
    	if T1.val==T2.val:
    		return self.isidentical(T1.left,T2.left) and self.isidentical(T1.right,T2.right)

    	else:
    		return False

















