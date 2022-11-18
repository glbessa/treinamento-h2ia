class List:
	@staticmethod
	def toStr(list_, sep=","):
		string = ""
		for i in list_:
			string += i+sep
		return string[:-1]