# The code below is the basic operations for the binary search tree

# 1: Tree traversal
#  Inorder tree walk

Inoder_tree_walk(x):
	if x !=None
		Inoder_tree_walk(x.left)
		print x.key
		Inoder_tree_walk(x.right)


# 2:Search the key value in the tree
Tree_Search(x,k):
	if x==None or k==x.key
		return x
	if k<x.key:
		return Tree_Search(x.left,k)
	else:
		return Tree_Search(x.right,k)

#  Or use the while loop to achive the recursion, 
	Iterative(x,k):
		while x != None and k != x.key:
			if k<x.key:
				x=x.left
			else x=x.right
		return x
