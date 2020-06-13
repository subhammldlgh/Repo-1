#computer uses O and player uses X
class Algo:
	def __init__(self):
		self.board = ['-','-','-',
					'-','-','-',
					'-','-','-',
					'-','-','-',]

	def check_win(self):  #check if player or computer has won
		win = False
		#horizontal win
		if self.board[0] == self.board[1] and self.board[1] == self.board[2] and self.board[2] != '-':
			win = True
		elif self.board[3] == self.board[4] and self.board[4] == self.board[5] and self.board[5] != '-':
			win = True
		elif self.board[6] == self.board[7] and self.board[7] == self.board[8] and self.board[8] != '-':
			win = True
	    #vertical win
		elif self.board[0] == self.board[3] and self.board[3] == self.board[6] and self.board[6] != '-':
			win = True
		elif self.board[1] == self.board[4] and self.board[4] == self.board[7] and self.board[7] != '-':
			win = True
		elif self.board[2] == self.board[5] and self.board[5] == self.board[8] and self.board[8] != '-':
			win = True
	    #diagonal win
		elif self.board[0] == self.board[4] and self.board[4] == self.board[8] and self.board[8] != '-':
			win = True
		elif self.board[2] == self.board[4] and self.board[4] == self.board[6] and self.board[6] != '-':
			win = True
		return win

	def check_draw(self):    #check for condition of draw
		draw = True
		for x in range(0,9):
			if self.board[x] == '-':
				draw = False
				break
		return draw

	def minimax(self, isAI):
		if self.check_win():  #if any one wins then true
			if isAI:          #if computer wins
				score = 1
			else:             #if player wins
				score = -1

		elif self.check_draw():  #if draw takes place
			score = 0
		
		else:
			#The next move is for the player. The player will want to minimize the score
			if isAI:
				bestScore = 1000
				bestMove = -1
				for x in range(0,9):
					if self.board[x]=="-":
						self.board[x] = 'X'
						moveScore = self.minimax(False)
						self.board[x] = '-'

						if moveScore<bestScore:
							bestScore = moveScore
							bestMove = x
						
				score = bestScore

			#The next move is for the computer. The computer will try to maximize the score
			else:
				bestScore = -1000
				bestMove = -1
				for x in range(0,9):
					if self.board[x]=="-":
						self.board[x] = 'O'
						moveScore = self.minimax(True)
						self.board[x] = '-'

						if moveScore>bestScore:
							bestScore = moveScore
							bestMove = x
				score =  bestScore
		return score

#bestScore stores the value of the best score from minimax and bestMove stores the locatio where computer should move O to
	def ai_choice(self):   #the computer chooses to put O and try for all plaecs to maximize its utility or score
		bestScore = -1000
		bestMove = -1
		for x in range(0,9):     #check all places one by one if not occupied
			if self.board[x]=="-":
				self.board[x] = 'O'
				moveScore = self.minimax(True)
				self.board[x] = '-'       #replace blank to try other places for O

				if moveScore>bestScore:     #maximize the bestScore
					bestScore = moveScore
					bestMove = x
		return bestMove


