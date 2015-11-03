#  Option 1:use the dfs, from other's code:

# Definition for a undirected graph node
class UndirectedGraphNode:
	def __init__(self, x):
		self.label = x
		self.neighbors = []


class Solution:
	def connectedSet(self, nodes):
		"""
		Connected component rather than clique
		:param nodes: {UndirectedGraphNode[]} nodes a array of undirected graph node
		:return: {int[][]} a connected set of a undirected graph
		"""
		rets = []
		visisted = set()
		for node in nodes:
			if node not in visisted: 
				# for i in rets:
				# 	if sorted(node.neighbors) == i:
				# 		i.append(node.label)
				# 	for j in node.neighbors:
				# 		if j in i and j.neighbors==[]:
				# 			i.append(node.label)
				# 			break
				ret = []
				self.dfs(node, visisted, ret)
				ret.sort()
				rets.append(ret)

		return rets

	def dfs(self, node, visited, ret):
		# pre-call check
		ret.append(node.label) #every time we call dfs,we will add this node to the visited set and 
								# add the label to the corresponding connected component
		visited.add(node)
		for nei in node.neighbors:
			if nei not in visited:
				self.dfs(nei, visited, ret)

# Optioan 2: bfs, my own code after reading other's code

# the problem i meet here is don't traversal the whole graph when we fix a point, which indirectly
# 	shows that I don't understant the queue function in the bfs totally. 
# from Queue import Queue

# class Solution:
# 	def connectedSet(self, nodes):
# 		"""
# 		Connected component rather than clique
# 		:param nodes: {UndirectedGraphNode[]} nodes a array of undirected graph node
# 		:return: {int[][]} a connected set of a undirected graph
# 		"""
# 		if not nodes:
# 			return []
# 		visited=set()
# 		cur=Queue(len(nodes))
# 		rets=[]
# 		for node in nodes:
# 			if node not in visited:
# 				cur.put(node)  #this is the queue when we walk through the whole graph
# 				visited.add(node)# this is the set we have ever traveled, include the black and gray verdices
# 				ret=[node.label]
# 				while(cur.empty() !=1):
# 					current_node=cur.get() #we pop out a node from the queue and walk this vertix in the next breadth
# 					for nei in current_node.neighbors:
# 						if nei not in visited:
# 							cur.put(nei)
# 							visited.add(nei)
# 							ret.append(nei.label)
# 					# c=cur.get()
# 					ret.sort() # use this line if we want the sorted lable 
# 				rets.append(ret)
# 		return rets

if __name__=='__main__':
	A=UndirectedGraphNode('A')
	B=UndirectedGraphNode('B')
	D=UndirectedGraphNode('D')
	C=UndirectedGraphNode('C')
	E=UndirectedGraphNode('E')
	F=UndirectedGraphNode('F')
	# G=UndirectedGraphNode('G')
	A.neighbors=[B,D]
	B.neighbors=[D]
	D.neighbors=[]
	C.neighbors=[E]
	E.neighbors=[]
	F.neighbors=[E,C]
	# G.neighbors=[E,F]

	nodes=[A,B,D,C,E,F]
	a=Solution()
	b=a.connectedSet(nodes)
	# for i in a.connectedSet(nodes):
	# 	print i