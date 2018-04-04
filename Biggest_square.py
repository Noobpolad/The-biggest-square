import random


class StartingPoint:

	def __init__(self):
		self.point = None
		self.width = 1

	#Reset	
	def update(self):
		self.point = None
		self.width = 1	


class Board:

	def __init__(self, board):
		self.board = board
		self.sp = StartingPoint()
		self.biggest_square = None

	#Check the square vertically	
	def checkColumns(self):
		for row in range(self.sp.point[0] - 1, self.sp.point[0] + self.sp.width + 1): #Start checking from the first row of the square - 1, till the last + 1
			for col in range(self.sp.point[1], self.sp.point[1] + self.sp.width):
				try:
					#Because in Python negative indexing allowed, we need to ignore it.
					if row < 0: 
						continue
					#If the height is more than space left	
					elif row == self.sp.point[0] and row + self.sp.width - 1 >= len(self.board): 
						return False
					#If we are at first row of the square - 1 or at	the last + 1 and at some possition of the row == to 1	
					elif (row == self.sp.point[0] - 1 and self.board[row][col] == 1) or (row == self.sp.point[0] + self.sp.width and self.board[row][col] == 1):
						return False
					#If we are inside the square and at some possition it == to 0	
					elif row != self.sp.point[0] - 1 and row != self.sp.point[0] + self.sp.width and self.board[row][col] == 0: 
						return False			
				except IndexError:
					continue	
		return True		

	#The same process as in colums, exept the checking goes horizontally and we dont need to include the case, when the width is more than space left
	def checkRows(self):
		for row in range(self.sp.point[0], self.sp.point[0] + self.sp.width):
			for col in range(self.sp.point[1] - 1, self.sp.point[1] + self.sp.width + 1):
				try:
					if col < 0:
						continue	
					elif (col == self.sp.point[1] - 1 and self.board[row][col] == 1) or (col == self.sp.point[1] + self.sp.width and self.board[row][col] == 1): 
						return False	
					elif col != self.sp.point[1] - 1 and col != self.sp.point[1] + self.sp.width and self.board[row][col] == 0:
						return False
				except IndexError:
					continue	
		return True	

	def visualize(self):
		for row in range(self.biggest_square[1]):
			print('---' * self.biggest_square[1])
			for col in range(self.biggest_square[1]):
				print('|1', end='|')
			print()
		print('---' * self.biggest_square[1])
		print('The initial point of the square:',self.biggest_square[0])
		print('The width and height of the square:',self.biggest_square[1])					

	def __call__(self):
		for row in range(len(self.board)):
			for col in range(len(self.board[row])):
				#Finish tracking and check if the square is correct
				if (self.sp.point != None and self.board[row][col] == 0) or (self.sp.point != None and col == len(self.board[row]) - 1): 
					if self.checkColumns() and self.checkRows():
						#If the biggest square is empty or the new one is bigger than the previous
						if (self.biggest_square == None) or (self.biggest_square != None and self.biggest_square[1] < self.sp.width):
							self.biggest_square = [self.sp.point, self.sp.width]
					#Reset the tracking at the end			
					self.sp.update()
				#Start tracking	
				elif self.board[row][col] == 1 and self.sp.point == None:
					self.sp.point = [row, col]
				#Continue tracking	
				elif self.board[row][col] == 1 and self.sp.point != None:
					self.sp.width += 1
		self.visualize()			

					
example =  [[1,1,0,0,0,0,1,1,1,1,0,0,0,0,0], 
			[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
			[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],  
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  
			[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],  
			[0,0,0,0,0,0,0,0,1,1,1,0,0,0,0],  
			[0,0,0,0,0,0,0,0,1,1,1,0,0,0,1],  
			[1,0,0,0,0,0,0,0,1,1,1,0,0,0,1],  
			[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],  
			[1,0,1,1,1,1,0,0,0,0,0,0,0,0,1]]  


board = Board(example)
board()