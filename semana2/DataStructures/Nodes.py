from __future__ import annotations

class Node:
	def __init__(self, value):
		self.value = value

	def __repr__(self):
		return f"({self.value})"

class TrackbackNode(Node):
	def __init__(self, value, parent:TrackbackNode=None):
		super().__init__(value)
		self.parent = parent

class TreeNode(TrackbackNode):
	def __init__(self, value, parent:TreeNode=None, children:list=list()):
		super().__init__(value, parent)
		self.children = children

class GraphNode(Node):
	def __init__(self, value, parents:list[GraphNode]=list(), children:list[GraphNode]=list()):
		super().__init__(value)
		self.parents = parents
		self.children = children

	def getNodeCardinality(self):
		return len(self.children)

class GraphNodeLabeledEdge(Node):
	def __init__(self, value, parents:list[GraphNodeLabeledEdge]=list(), children:dict[str, GraphNodeLabeledEdge]=dict()):
		super().__init__(value)
		self.parents = parents
		self.children = children

	def getNodeCardinality(self):
		return len(self.children)

class GraphNodeWeightedEdge(Node):
	def __init__(self, value, parents:list[GraphNodeWeightedEdge]=list(), children:dict[str, GraphNodeWeightedEdge]=dict()):
		super().__init__(value)
		self.parents = parents
		self.children = children

	def getNodeCardinality(self):
		return len(self.children)