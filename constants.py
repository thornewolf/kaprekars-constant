import networkx as nx
import matplotlib.pyplot as plt

def magic(n):
	c=0
	path = [n]
	while n != 6174:
		if n == 0:
			return path
		c += 1
		rsn = ''.join(sorted(str(n)))
		sn = rsn[::-1]
		rsn = int(rsn)
		sn = int(sn)
		#print(sn,rsn)
		n = sn-rsn
		path.append(n)
	return path

class Node:
	def __init__(self,n):
		self.value = n
		self.amount = 1
		self.children = []
	def addChild(self,n):
		'''
		Returns (created child [Node], new entry? [bool])
		'''
		found = False
		for child in self.children:
			if n == child.value:
				found = True
				child.amount += 1
				return child, False
		child = Node(n)
		self.children.append(child)
		return child, True
	def __str__(self):
		return str(self.value)


LOW = 1000
HIGH = 10000
paths = [magic(i) for i in range(LOW,HIGH)]
paths = [i[::-1][1:] for i in paths if i[-1]==6174]
#print(paths)
magic_node = Node(6174)
G=nx.DiGraph()



l = len(paths)
for path in paths[:l//20]:
	currentNode = magic_node
	for number in path:
		oldNode, currentNode, new = currentNode, *currentNode.addChild(number)
		G.add_node(currentNode)
		G.add_edge(currentNode,oldNode)
		#print(currentNode)



pos = nx.drawing.spring_layout(G,k=1,scale=10)
'''for i in pos:
        pos[i][0] = pos[i][0] * 2000 # x coordinate
        pos[i][1] = pos[i][1] * 20000000 # y coordinate
'''


nx.draw(G,with_labels=True,font_size=3,node_size=50)
plt.show()


