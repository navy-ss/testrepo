"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def num_occupied(board):
    num = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                num += 1
    return num


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    if board == initial_state():
        return X
    else:
        occupied = num_occupied(board)
        if occupied % 2 == 1:
            return O
        elif occupied % 2 == 0:
            return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
    	for j in range(3):
    		if board[i][j] == EMPTY:
    			val = (i, j)
    			possible_actions.add(val)
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]
    newboard = copy.deepcopy(board)

    if board[i][j] == EMPTY:
    	newboard[i][j] = player(newboard)
    	return newboard
    else:
    	raise Exception("Invalid Move")
    	    	


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] == board[0][2] == X:
    	return X
    if board[1][0] == board[1][1] == board[1][2] == X:
    	return X
    if board[2][0] == board[2][1] == board[2][2] == X:
    	return X
    if board[0][0] == board[1][0] == board[2][0] == X:
    	return X
    if board[0][1] == board[1][1] == board[2][1] == X:
    	return X
    if board[0][2] == board[1][2] == board[2][2] == X:
    	return X
    if board[0][0] == board[1][1] == board[2][2] == X:
    	return X
    if board[2][0] == board[1][1] == board[0][2] == X:
    	return X

    if board[0][0] == board[0][1] == board[0][2] == O:
    	return O
    if board[1][0] == board[1][1] == board[1][2] == O:
    	return O
    if board[2][0] == board[2][1] == board[2][2] == O:
    	return O
    if board[0][0] == board[1][0] == board[2][0] == O:
    	return O
    if board[0][1] == board[1][1] == board[2][1] == O:
    	return O
    if board[0][2] == board[1][2] == board[2][2] == O:
    	return O
    if board[0][0] == board[1][1] == board[2][2] == O:
    	return O
    if board[2][0] == board[1][1] == board[0][2] == O:
    	return O
    else:
    	return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    else:
        for y in range(3):
            for x in range(3):
                if board[y][x] == EMPTY:
                    return False
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
    	return 1
    elif winner(board) == O:
    	return -1
    else:
    	return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    opt_action = (-1,-1)

    if terminal(board):
    	return None

    def max_value(board):
    	if terminal(board):
    		return utility(board)
    	v_max = -math.inf
    	for action in actions(board):
    		v_max = max(v_max, min_value(result(board, action)))
    	return v_max

    def min_value(board):
    	if terminal(board):
    		return utility(board)
    	v_min = math.inf
    	for action in actions(board):
    		v_min = min(v_min, max_value(result(board, action)))
    	return v_min

    if player(board) == X:
    	v = -math.inf
    	for action in actions(board):
    		t = min_value(result(board, action))
    		if t > v:
    			v = t
    			opt_action = action
    else:
    	v = math.inf
    	for action in actions(board):
            t = max_value(result(board, action))
            if t < v:
                v = t
                opt_action = action

    return opt_action
