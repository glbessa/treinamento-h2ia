from collections import deque
from DataStructures.Nodes import TreeNode, TrackbackNode

def exploreNeighbors(map, x, y, ocuppiedSymbol, nodeType=TrackbackNode):
	possible_neighbors = list()

	for j, i in [(-1,0), (1,0), (0,-1), (0,1)]:
		if (map[y + i][x + j] != ocuppiedSymbol):
			possible_neighbors.append(nodeType(value=f"{x+j},{y+i}"))
	return possible_neighbors

def checkGoal(actualNode, goalNode):
	if actualNode.value == goalNode.value:
		return True
	return False

def breadthFirstSearch(map, ocuppiedSymbol, initialNode, goalNode):
	tree = initialNode
	actualNode = initialNode
	visitedNodes = dict()
	nextNodes = deque()
	optimalPath = list()
	optimalCost = 0
	
	while not(checkGoal(actualNode, goalNode)):
		actualNodeX = int(actualNode.value.split(',')[0])
		actualNodeY = int(actualNode.value.split(',')[1])

		neighbors = exploreNeighbors(map, actualNodeX, actualNodeY, ocuppiedSymbol)

		for neighbor in neighbors:
			if not(neighbor.value in visitedNodes):
				neighbor.parent = actualNode
				nextNodes.append(neighbor)

		if len(nextNodes) == 0:
			return None

		actualNode = nextNodes.popleft()

	while actualNode.parent != None:
		optimalCost += 1
		optimalPath.append(actualNode)
		actualNode = actualNode.parent
	
	optimalPath.append(actualNode)

	optimalPath.reverse()

	return optimalPath, optimalCost

def depthFirstSearch(map, ocuppiedSymbol, initialNode, goalNode):
	actualNode = TrackbackNode(initialNode.value)
	visitedNodes = dict()
	nextNodes = deque()
	optimalPath = list()
	optimalCost = 0
	
	while not(checkGoal(actualNode, goalNode)):
		actualNodeX = int(actualNode.value.split(',')[0])
		actualNodeY = int(actualNode.value.split(',')[1])

		neighbors = exploreNeighbors(map, actualNodeX, actualNodeY, ocuppiedSymbol)

		for neighbor in neighbors:
			if not(neighbor.value in visitedNodes):
				neighbor.parent = actualNode
				nextNodes.append(neighbor)

		if len(nextNodes) == 0:
			return None

		visitedNodes.update({actualNode.value:None})
		actualNode = nextNodes.pop()

	while actualNode.parent != None:
		optimalCost += 1
		optimalPath.append(actualNode)
		actualNode = actualNode.parent
	
	optimalPath.append(actualNode)

	optimalPath.reverse()

	return optimalPath, optimalCost

def read_mapfile(filename, initialSymbol, goalSymbol):
	map = list()
	initialNode = None
	goalNode = None

	with open(filename, "r") as reader:
		content = reader.readlines()
		for i, line in enumerate(content):
			line = line.replace("\n", "").replace("\r", "")
			mapLine = list()
			for j, value in enumerate(line):
				mapLine.append(value)
				if value == initialSymbol:
					initialNode = TreeNode(f"{j},{i}")
				elif value == goalSymbol:
					goalNode = TreeNode(f"{j},{i}")
			map.append(mapLine)
	return map, initialNode, goalNode

if __name__ == "__main__":
	goalSymbol = "B"
	initialSymbol = "A"
	ocuppiedSymbol = "#"
	map, initialNode, goalNode = read_mapfile("map1.txt", initialSymbol, goalSymbol)
	print(depthFirstSearch(map, ocuppiedSymbol, initialNode, goalNode))

