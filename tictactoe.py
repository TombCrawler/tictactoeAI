"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


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
    Must start with X 
    """
    x_count = 0
    o_count = 0
    for i in range(len(board)): # row
        for j in range(len(board[0])): # column [j] on pstion [0] which is the first row having 3 elements
            if board[i][j] == X:
                x_count += 1
            if board[i][j] == O: # Do not use elif cz it gets empty cells for O
                o_count += 1

    # if terminal(board):
    #     return None
    # elif x_count == o_count:
    #     return X
    # else:
    #     return O 
    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_list = set()
    for i in range(len(board)):
        for j in range(len(board[i])): # column [j] on pstion [i] which is the first row having 3 elements
            if board[i][j] == EMPTY:
                actions_list.add((i, j))
    return actions_list


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board): 
        print(f"Hey!{action}")
        raise Exception("Not available")
    
    i, j = action 
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


# def winRow(board, player):
#     for i in range(len(board)):
#         if board[i][0] == player and board[i][1] == player and board[i][2] == player:
#             return True
#     return False


# def winCol(board, player):
#     for j in range(len(board)):
#         if board[0][j] == player and board[1][j] == player and board[2][j] == player:
#             return True
#     return False
    

# def winDiag1(board, player):
#     count = 0
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             if i == j and board[i][j] == player: # (0,0)(1,1)(2,2) gives a diagonal win and ==board[i][j] == player means the diagonal is the same player
#                 count += 1
#     if count == 3:
#         return True
#     else:
#         return False
    

# def winDiag2(board, player):
#     count = 0
#     for i in range(len(board)):
#         for j in range(len(board[i])): 
#             if (len(board) - i - 1) == j and board[i][j] == player: # len(board)-i-1) is for the opposite diagonal, refered to mario pyramid
#                 count +=1
#     if count == 3:
#         return True
#     else:
#         return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    [i][number]'s [i] means random, any row/ column being checked
    """
    for i in range(3):
        # Check if there is a winner in a row
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        # Check if there is a winner in a column
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]
    # Check if there is a winner in the two diagonals, if you draw the board, you will understand it
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None
    
    # if winRow(board, X) or winCol(board, X) or winDiag1(board, X) or winDiag2(board, X):
    #     return X
    # elif winRow(board, O) or winCol(board, O) or winDiag1(board, O) or winDiag2(board, O):
    #     return O
    # else:
    #     return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X:
        return True
    if winner(board) == O:
        return True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                return False # means no result yet cz there are still empty cells
    return True # this means the result is a Tie

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0 


def max_value(board):
    v= -math.inf # this comes with the math module
    if terminal(board):
        return utility(board)
    for action in actions(board):
      v = max(v, min_value(result(board, action)))  
    
    return v


def min_value(board):
    v= math.inf # this comes with the math module
    if terminal(board):
        return utility(board)
    for action in actions(board):
      v = min(v, max_value(result(board, action)))  
    
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    elif player(board) == X:
        plays = []
        for action in actions(board):
           plays.append([min_value(result(board, action)), action]) # result(board, action is the action we take, action is the action we took
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1] # reverse cz X palyer wants max value, [0] takes the 1st element and [1] takes the action

                       

    # Case of player is O
    elif player(board) == O:
        plays = []
        for action in actions(board):
           plays.append([max_value(result(board, action)), action]) # result(board, action is the action we take, action is the action we took
        return sorted(plays, key=lambda x: x[0])[0][1] # no need to reverse as we get the min value already






