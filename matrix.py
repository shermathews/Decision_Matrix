"""represents a decision-making matrix"""

class Matrix:
	def __init__(
		self,
		columns,
		rows,
		x_axis,
		y_axis
	):
		self.columns = columns
		self.rows = rows
		self.x_axis = x_axis
		self.y_axis = y_axis
		self.data = [[""] * (columns + 4) for item in range(rows + 4)]
		self.weights = [1 for item in range(rows)]
	
	def populate(self):
		"""populates decision matrix"""
		
		#Headers
		for x in range(self.columns):
			self.data[0][x+1] = self.x_axis[x]
			
		#Dimensions
		for y in range(self.rows):
			self.data[y+1][0] = self.y_axis[y]
		
		#Weights
		self.data[self.rows + 3][0] = "Weights"
		for i in range(self.rows):
			self.data[self.rows + 2][i + 1] = self.y_axis[i]
			self.data[self.rows + 3][i + 1] = self.weights[i]

		#Total
		self.data[self.rows + 1][0] = "Total"
		wArray = "b%d:%s%d" % (self.rows + 4, chr(self.rows + ord('a')), self.rows + 4)
		dArray = "b2:%s%d" % (chr(self.rows + 1 + ord('a')), self.rows + 1)
		self.data[self.rows + 1][1] = "=mmult(%s, %s)" % (wArray, dArray)	