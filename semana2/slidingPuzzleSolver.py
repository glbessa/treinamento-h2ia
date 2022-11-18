from __future__ import annotations

from collections import deque
import random
import time
from DataStructures.Nodes import TreeNode, TrackbackNode
from DataStructures.Matrix import Matrix
from DataStructures.List import List

OPERATIONS = {
		(-1,0):0,
		(1,0):1,
		(0,-1):2,
		(0,1):3
	}

OPERATIONS_LABELS = {
		0:"esquerda",
		1:"direita",
		2:"acima",
		3:"abaixo"
	}

class SpecialNode(TrackbackNode):
	def __init__(self, value, blankPos, parent:SpecialNode=None, operation:int=None):
		super().__init__(value, parent)
		self.operation = operation
		self.blankPos = blankPos

	def __repr__(self):
		return f"({self.value}, {self.blankPos}, {OPERATIONS_LABELS.get(self.operation)})"

def generateSlidingPuzzle(width, height):
	blockValues = [ str(i) for i in range(1, height * width) ]
	blockValues.append('X')
	random.shuffle(blockValues)
	matrix = Matrix.fromList(blockValues, width, height)
	return matrix, Matrix.search(matrix, 'X')

def generateFinalSlidingPuzzle(width, height):
	blockValues = [ str(i) for i in range(1, height * width) ]
	blockValues.append('X')
	return Matrix.fromList(blockValues, width, height)

def numberOfInvertions(puzzle):
	puzzleList = Matrix.toList(puzzle)
	counter = 0
	for i, b in enumerate(puzzleList):
		for j, a in enumerate(puzzleList):
			if (a > b) and (j < i):
				counter += 1
	return counter

def validatePuzzle(puzzle, width, blankPos):
	nInv = numberOfInvertions(puzzle)
	if width % 2 == 1:
		return nInv % 2 == 0
	elif width % 2 == 0	:
		rowRevInd = width - (blankPos[1] + 1)
		if (rowRevInd % 2 == 0) and (nInv % 2 == 1):
			return True
		elif (rowRevInd % 2 == 1) and (nInv % 2 == 0):
			return True
	return False

def exploreNeighbors(puzzle, x, y):
	possibleNeighbors = list()
	for j, i in [(-1,0), (1,0), (0,-1), (0,1)]:
		if not((len(puzzle) <= i + y) or (len(puzzle[0]) <= j + x) or (0 > i + y) or (0 > j + x)):
			newPuzzle = Matrix.copy(puzzle)
			temp = newPuzzle[y][x]
			if temp != "X":
				exit()
			newPuzzle[y][x] = puzzle[y+i][x+j]
			newPuzzle[y+i][x+j] = temp
			possibleNeighbors.append(SpecialNode(value=Matrix.toStr(newPuzzle), blankPos=(x+j, y+i) , operation=OPERATIONS.get((j,i))))
	return possibleNeighbors

def checkGoal(actualNode, goalNode):
	return actualNode.value == goalNode.value

def breadthFirstSearch(initialNode, width, height, goalNode):
	actualNode = initialNode
	visitedNodes = dict()
	nextNodes = deque()
	optimalPath = list()
	
	while not(checkGoal(actualNode, goalNode)):
		neighbors = exploreNeighbors(Matrix.fromStr(actualNode.value, width, height), actualNode.blankPos[0], actualNode.blankPos[1])
		for neighbor in neighbors:
			if not(neighbor.value in visitedNodes):
				neighbor.parent = actualNode
				nextNodes.append(neighbor)

		#print(nextNodes)

		if len(nextNodes) == 0:
			return None

		visitedNodes.update({actualNode.value:None})
		actualNode = nextNodes.popleft()

	while actualNode.parent != None:
		optimalPath.append(actualNode)
		actualNode = actualNode.parent
	
	optimalPath.append(actualNode)

	optimalPath.reverse()

	return optimalPath

def depthFirstSearch(initialNode, width, height, goalNode):
	actualNode = initialNode
	visitedNodes = dict()
	nextNodes = deque()
	optimalPath = list()
	
	while not(checkGoal(actualNode, goalNode)):
		
		neighbors = exploreNeighbors(Matrix.fromStr(actualNode.value, width, height), actualNode.blankPos[0], actualNode.blankPos[1])
		
		for neighbor in neighbors:
			if not(neighbor.value in visitedNodes):
				neighbor.parent = actualNode
				nextNodes.append(neighbor)

		if len(nextNodes) == 0:
			return None

		visitedNodes.update({actualNode.value:None})
		actualNode = nextNodes.pop()

	while actualNode.parent != None:
		optimalPath.append(actualNode)
		actualNode = actualNode.parent
	
	optimalPath.append(actualNode)

	optimalPath.reverse()

	return optimalPath

def visualizePath(path, width, height):
	for state in path:
		print(f"Operation: {OPERATIONS_LABELS.get(state.operation)}   =>")
		Matrix.print(Matrix.fromStr(state.value, width, height))
		print()

if __name__ == "__main__":
	width = 4
	height = width
	puzzle, blankPos = generateSlidingPuzzle(width, height)

	while not(validatePuzzle(puzzle, width, blankPos)):
		puzzle, blankPos = generateSlidingPuzzle(width, height)
	
	print()
	Matrix.print(puzzle)
	print()

	blockValues = [ str(i) for i in range(1, width * height) ]
	blockValues.append('X')
	finalPuzzleNode = SpecialNode(value=List.toStr(blockValues), blankPos=(width-1, height-1))

	initialNode = SpecialNode(value=Matrix.toStr(puzzle), blankPos=blankPos)

	start = time.time()
	path = breadthFirstSearch(initialNode, width, height, finalPuzzleNode)
	#path = depthFirstSearch(initialNode, width, height, finalPuzzleNode)
	end = time.time()
	delta = end-start

	if path != None:
		visualizePath(path, width, height)
		print(f"Custo: {len(path)-1} | Tempo decorrido: {delta:.2f}s")
	else:
		print("Não foi possível obter um caminho")
		print(f"Tempo decorrido: {delta:.2f}s")