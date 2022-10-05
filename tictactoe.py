"""
Tic Tac Toe Player
"""
import sys
import math
import copy

X = "X"
O = "O"
EMPTY = None

class InvalidActionException(Exception):
    pass

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
    if board == initial_state(): return X
    return O if sum(board, []).count(X) > sum(board,[]).count(O) else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return { (int(key/3),key % 3) for key, val in enumerate(sum(board, [])) if val == EMPTY }


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        #print(board, actions(board))
        raise InvalidActionException
    nBoard = copy.deepcopy(board)
    nBoard[action[0]][action[1]] = player(board)
    return nBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # None to string
    b = [[str(val) for val in row] for row in board]
    # check horizontally
    for key, row in enumerate(board):
        if all(el == X for el in row): return X
        if all(el == O for el in row): return O
    # check vertically
    if b[0][0]+b[1][0]+b[2][0] == 'XXX': return X
    if b[0][0]+b[1][0]+b[2][0] == 'OOO': return O
    if b[0][1]+b[1][1]+b[2][1] == 'XXX': return X
    if b[0][1]+b[1][1]+b[2][1] == 'OOO': return O
    if b[0][2]+b[1][2]+b[2][2] == 'XXX': return X
    if b[0][2]+b[1][2]+b[2][2] == 'OOO': return O
    # check diagonally
    if b[0][0]+b[1][1]+b[2][2] == 'XXX': return X
    if b[0][0]+b[1][1]+b[2][2] == 'OOO': return O
    if b[0][2]+b[1][1]+b[2][0] == 'XXX': return X
    if b[0][2]+b[1][1]+b[2][0] == 'OOO': return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board): return True
    for row in board:
        if None in row: return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X: return 1
    if winner(board) == O: return -1
    return 0



# returns (action, evaluation)
def _minimax(board, parent_action, maximizingPlayer=True):

    if terminal(board): return parent_action, utility(board)

    # generate next nodes
    _boards = [{'board': result(board, ac), 'parent_action': ac} for ac in actions(board)]

    if maximizingPlayer:
        maxEvaluation = float('-inf')
        maximizingAction = list(actions(board))[0]
        for b in _boards:
            (optimal_action, evaluation) = _minimax(b.get('board'), b.get('parent_action'), False)
            if evaluation >= maxEvaluation:
                maxEvaluation = evaluation
                maximizingAction = optimal_action

        return maximizingAction, maxEvaluation

    else:
        minEvaluation = float('inf')
        minimizingAction = list(actions(board))[0]
        for b in _boards:
            (optimal_action, evaluation) = _minimax(b.get('board'), b.get('parent_action'), True)
            if evaluation < minEvaluation:
                minEvaluation = evaluation
                minizingAction = optimal_action

        return minimizingAction, minEvaluation



def minimax(board, act=None):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board): return None


    # action, eval = _minimax(board, None, False if player(board) == X else True)
    action, eval = _minimax(board, None, True)
    print("res: ", action, eval)
    return action
