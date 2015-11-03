"""
Convert a binary search tree to doubly linked list with in-order traversal.

Example:
Given a binary search tree:
    4
   / \
  2   5
 / \
1   3

return 1<->2<->3<->4<->5

"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition of Doubly-ListNode
class DoublyListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = next
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class DoublyListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = next

class Solution:
    """
    @param root, the root of tree
    @return: a doubly list node

    refer to binary_tree_inorder_traversal.py

    the key of this problem is to realize the in order traversal in 
    binary tree, i still not come up with the idea. 
    Again, i don't understand the why we use stack and cur as our 
    discriminent. cur is the node we want to explore, we don't know whether
    it is none or not, and this is the essential for the if-else, if it is 
    None, well, just pop out the element from the stack, if not, we need to 
    keep adding the element in the stack.

    Notice i first use cur.left as to judge the left node is None, which is 
    not working, since every time we pop out the element, we will be aigin 
    in this circle. 
    """
    def bstToDoublyList(self, root):
        # Write your code here
        if not root:
        	return None
        stack=[]
        cur=root
        res=[]
        while (stack or cur ):
        	if cur:
        		stack.append(cur)
        		cur=cur.left
        	else:
        		cur=stack.pop()
        		res.append(cur.val)
        		cur=cur.right
        # connect the linked list given the in-order traversal of the tree
        head=DoublyListNode(res[0])
        prev=head
        for i in xrange(1,len(res)):
        	cur=DoublyListNode(res[i])
        	prev.next=cur
        	cur.prev=prev
        	prev=cur

        return head




if __name__=='__main__':
	a=TreeNode(1)
	b=TreeNode(2)
	c=TreeNode(3)
	a.right=b
	b.left=c
	print Solution().bstToDoublyList(a)



        	










