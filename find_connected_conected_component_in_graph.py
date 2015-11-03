# Find the number connected component in the undirected graph.
 # Each node in the graph contains a label and a list of its neighbors. 
 # (a connected component (or just component) of an undirected graph is a subgraph 
 # in which any two vertices are connected to each other by paths, and which is
  # connected to no additional vertices in the supergraph.)

# 	In real case, need to ask the intervier: can we assume the given nodes are valid, so that we only
# need to check for success case? That means, we assume for example a linear list A-B-C does not exist.

# 	In the code, in order to distinguish the color from the node, we use a set to store the 
# visited nodes, The reson for that is that the set is unrepeaded and is convenient to check
# (if i in visited).

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
from Queue import Queue

class Solution:
	def connectedSet(self, nodes):
		"""
		Connected component rather than clique
		:param nodes: {UndirectedGraphNode[]} nodes a array of undirected graph node
		:return: {int[][]} a connected set of a undirected graph
		"""
		if not nodes:
			return []
		visited=set()
		cur=Queue(len(nodes))
		rets=[]
		for node in nodes:
			if node not in visited:
				cur.put(node)  #this is the queue when we walk through the whole graph
				visited.add(node)# this is the set we have ever traveled, include the black and gray verdices
				ret=[node.label]
				while(cur.empty() !=1):
					current_node=cur.get() #we pop out a node from the queue and walk this vertix in the next breadth
					for nei in current_node.neighbors:
						if nei not in visited:
							cur.put(nei)
							visited.add(nei)
							ret.append(nei.label)
					# c=cur.get()
					ret.sort() # use this line if we want the sorted lable 
				rets.append(ret)
		return rets

if __name__=='__main__':
	A=UndirectedGraphNode('A')
	B=UndirectedGraphNode('B')
	D=UndirectedGraphNode('D')
	C=UndirectedGraphNode('C')
	E=UndirectedGraphNode('E')
	F=UndirectedGraphNode('F')
	G=UndirectedGraphNode('G')
	A.neighbors=[B,D]
	B.neighbors=[A,C]
	D.neighbors=[A,C]
	C.neighbors=[B,D]
	E.neighbors=[F,G]
	F.neighbors=[E,G]
	G.neighbors=[E,F]

	nodes=[A,B,D,C,E,F,G]
	a=Solution()
	b=a.connectedSet(nodes)
	# for i in a.connectedSet(nodes):
	# 	print i











