from .List import List

class Matrix:
	@staticmethod
	def toStr(matrix, sep=","):
		converted = ""
		for line in matrix:
			for item in line:
				converted += item + sep
		return converted[:-1]

	@staticmethod
	def fromStr(string, width, height, sep=","):
		matrix = list()
		string = string.split(sep)
		for i in range(height):
			line = list()
			for j in range(width):
				line.append(string[(height * i) + j])
			matrix.append(line)
		return matrix
			
	@staticmethod
	def toList(matrix):
		list_ = list()
		for line in matrix:
			list_.extend(line)
		return list_

	@staticmethod
	def fromList(list_, width, height):
		list_.reverse()
		matrix = list()
		for i in range(height):
			line = list()
			for j in range(width):
				line.append(list_.pop())
			matrix.append(line)

		return matrix

	@staticmethod
	def copy(matrix):
		newMatrix = list()
		for line in matrix:
			newMatrix.append(line.copy())
		return newMatrix

	@staticmethod
	def search(matrix, item):
		itemPos = None
		for i, line in enumerate(matrix):
			for j, value in enumerate(line):
				if value == item:
					itemPos = (j, i)
		return itemPos

	@staticmethod
	def print(matrix):
		for line in matrix:
			print(List.toStr(line, " "))
		
