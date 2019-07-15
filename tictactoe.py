from IPython.display import clear_output

def print_board(board):
	def one_line(line):
		print("{}|{}|{}".format(line[0], line[1], line[2]))
	def long_line():
		print("------")
	one_line(board[0])
	long_line()
	one_line(board[1])
	long_line()
	one_line(board[2])
	print("\n\n")

def player_move(player, move, board, open_spaces):
	if move in open_spaces:
		open_spaces.remove(move)
		for x in board:
			count = 0
			for y in x:
				if y == move:
					x.remove(move)
					x.insert(count, player)
				count += 1
		return True
	else:
		return False

def test_board(board):
	for x in board:
		if x[0] == x[1] and x[0] == x[2]:
			print("winner " + x[0])
			return True
	for x in range(3):
		if board[0][x] == board[1][x] and board[0][x] == board[2][x]:
			print("winner " + board[0][x])
			return True 
	if(board[0][0] == board[1][1] and board[0][0] == board[2][2]):
		print("winner " + board[0][0])
		return True
	if(board[0][2] == board[1][1] and board[0][2] == board[2][0]):
		print("winner " + board[0][2])
		return True
	return False

while True:
	total_move = 0
	board = [["1","2","3"], ["4","5","6"], ["7","8","9"]]
	open_spaces = ["1", "2", "3", "4", "5", "6","7", "8","9"]
	while True:
		player = input("Who goes first X or O?  ")
		player = player.upper()
		if player == "X" or player == "O":
			break
		print("Please enter X or O")

	while total_move < 9:
		print('\n'*100)
		print_board(board)
		if test_board(board):
			break
		if player == "X":
			while True:
				move = input("Player X turn:  ")
				if player_move("X", move, board, open_spaces):
					break
			player = "O"
		else:
			while True:
				move = input("Player O turn:  ")
				if player_move("O", move, board, open_spaces):
					break

			player = "X"
		total_move += 1
	while True:
		test = input("New Game Y/N?  ")
		if test.lower() == "n":
			quit()
		if  test.lower() == "y":
			break
		print("please answer Y/N ")

