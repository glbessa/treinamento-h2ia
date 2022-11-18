from .Nodes import GraphNode, GraphNodeLabeledEdge, GraphNodeWeightedEdge

class Graph:
	@staticmethod
	def adjacencyMatrixToGraph(adjacencyMatrix, labels:list=None):
		for line in adjacencyMatrix:
			if len(adjacencyMatrix) != len(line):
				return None
		
		if labels == None:
			labels = [ i for i in range(len(adjacencyMatrix))]

		initialNode = GraphNode(labels[0])

'''
class EulerPath:
	@staticmethod
	def hasEulerPath(graph:Graph):
		oddDegreeNodes = 0
		for index in range(len(graph)):
			if graph.getNodeDegree(index) % 2 != 0:
				oddDegreeNodes += 1
		if (oddDegreeNodes == 0) or (oddDegreeNodes == 2):
			return True
		return False

	@staticmethod
	def getEulerPaths(graph:Graph):
		if !(hasEulierPath(graph)):
			return None
		for index in range(len(graph)):
			if graph.getNodeDegree(index)

class Graph:
	def __init__(self, matrix):
		self.matrix = matrix

	def __len__(self):
		return len(self.matrix)

	def __repr__(self):
		return self.matrix

	def insertNode(self, nodeEdges):
		pass

	def modifyNode(self, nodeIndex, nodeEdges):
		pass

	def removeNode(self, nodeIndex):
		pass
	
	def getNextNodes(nodeIndex):
		nextNodes = list()
		for index, value in enumerate(map[nodeIndex]):
			if value == 1:
				nextNodes.append(index)
		return nextNodes

	def hasInitialNode(self):
		for i in self.matrix:
			initialNode = True
			for j in i:
				if j != 0:
					initialNode = False
			if initialNode:
				return True
		return False

	def getNodeDegree(self, nodeIndex):
		degree = 0
		for index, value in enumerate(self.matrix[nodeIndex]):
			if index == nodeIndex:
				continue
			if value != 0:
				degree += 1
		return degree

class NodeLabeledGraph(Graph):
	def __init__(self, matrix:list, nodeLabels:dict):
		super().__init__(matrix)
		self.nodeLabels = nodeLabels

	def getNodeIndex(self, nodeLabel):
		return nodeLabels[nodeLabel]

	def getNodeLabel(self, nodeIndex):
		pass

class EdgeLabeledGraph(Graph):
	def __init__(self, matrix:list, edgeLabels:list):
		super().__init__(matrix)
		self.edgeLabels = edgeLabels

class NodeEdgeLabeledGraph(NodeLabeledGraph):
		self.edgeLabels = edgeLabels
		
	def __init__(self, matrix, nodeLabels:list, edgeLabels:list):
		super().__init__(matrix, nodeLabels)
'''