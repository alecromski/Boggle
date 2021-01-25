#! /usr/bin/python3
def make_board(letters, board_dimensions):
	board = [[None for i in range(board_dimensions+2)] for i in range(board_dimensions+2)]
	position = {}
	x = 0
	y = 0
	for letter in letters:
		position[x, y] = letter.lower()
		y += 1
		if y >= board_dimensions:
			y = 0
			x += 1

	for (x, y) in position:
		board[x+1][y+1] = position[(x,y)]
	return board, position

def get_neighbors(board, current_position):
	result = []
	x, y = current_position
	a, b = x-1, y-1
	neighbors = [(board[x-1][y-1], (a-1,b-1)), (board[x-1][y], (a-1,b)), \
				(board[x-1][y+1], (a-1, b+1)), (board[x][y-1], (a, b-1)), \
				(board[x][y+1], (a,b+1)), (board[x+1][y-1], (a+1, b-1)), \
				(board[x+1][y], (a+1, b)), (board[x+1][y+1], (a+1, b+1))]

	neighbors = [n for n in neighbors if n[0]]
	return neighbors

def make_graph(board, position):
	graph = {}
	for node in position:
		graph[(position[node], node)] = get_neighbors(board, (node[0]+1, node[1]+1))
	graph[('', (None, None))] = [(position[node], node) for node in position]
	return graph	

