class Board:
	def __init__(self, matrix):
		self.matrix = [['' for x in range(8)] for y in range(8)]
		current = 'X'
		for i in range (0, 8):
			if (i%2 == 0):
				current = 'X'
			else:
				current = 'O'
			for j in range (0, 8):
				self.matrix[i][j] = current
				if (current == 'X'):
					current = 'O'
				else:
					current = 'X'

	#returns (-1, -1) if illegal move, otherwise returns move with right coords
	def convertMove(self, row, col):
		if (row < 1 || col < 1 || row > 8 || col > 8):
			return (-1, -1)
		return (row-1, col-1)


	def displayBoard(self):
		print("  ")
		for i in range (1, 9):
			print(i + "  ")
	
		for i in range (0, 8):
			print("\n" + (i+1) + "  ")
			for j in range (0, 8):
				print(self.matrix[i][j] + " ")


	def isLegalMove(self, turn, moves):
		for i in range (0, len(moves)):
			moves[i] = moves[i] - 1
			if (moves[i] < 0 || moves[i] > 7):
				return False
		if (len(moves) == 2):
			#removing
			if (matrix[moves[0]][moves[1]] == turn):
				matrix[moves[0]][moves[1]] = '.'
				return True
			else:
				return False
		else if (len(moves) % 2 == 1):
			return False
		else:
			#moving
			index = 0
			while (index < len(moves)-3):
				curRow = moves[index]
				curCol = moves[index+1]
				nextRow = moves[index+2]
				nextCol = moves[index+3]
				if (curRow == nextRow):
					if (abs(curCol-nextCol) == 2):
						#
						if (matrix[curRow][curCol] == turn && matrix[nextRow][nextCol] == '.' && matrix[curRow][(curCol+nextCol)/2] != turn && matrix[curRow][(curCol+nextCol)/2] != '.'):
							matrix[curRow][curCol] = '.'
							matrix[curRow][(curCol+nextCol)/2] = '.'
							matrix[nextRow][nextCol] = turn
						else:
							return False
					else:
						return False
				else if (curCol == nextCol):
					if (abs(curRow-nextRow) == 2):
						#
						#same
					else:
						return False
				else:
					return False



