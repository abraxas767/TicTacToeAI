from tictactoe import *

_ = None

test_boards = [

    [[X,O,_], # 0
     [_,_,_],
     [_,_,_]],

    [[_,_,_], # 1
     [_,_,_],
     [_,_,_]],

    [[X,O,X], # 2
     [O,_,_],
     [_,_,_]],

    [[X,O,X], # 3
     [O,X,_],
     [_,_,_]],

    [[X,O,X], # 4
     [O,X,O],
     [X,_,_]],

    [[X,O,X], # 5
     [O,X,O],
     [X,O,X]],

    [[X,O,X], # 6
     [O,_,O],
     [X,O,X]],

    [[X,_,_], # 7
     [_,_,_],
     [_,_,_]],
]

def test_player():
    assert player(test_boards[0]) == X, "Should be X"
    assert player(test_boards[1]) == X, "Should be X"
    assert player(test_boards[2]) == X, "Should be X"
    assert player(test_boards[3]) == O, "Should be O"
    assert player(test_boards[4]) == O, "Should be O"
    assert player(test_boards[6]) == X, "Should be X"


def test_actions():
    assert actions(initial_state()) == {(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)}
    assert actions(test_boards[2]) == {(1,1),(1,2),(2,0),(2,1),(2,2)}
    assert actions(test_boards[4]) == {(2,1),(2,2)}
    assert actions(test_boards[5]) == set()
    assert actions(test_boards[6]) == {(1,1)}

def test_result():
    assert result(test_boards[6], (1,1)) == test_boards[5]
    assert result(test_boards[2], (1,1)) == test_boards[3]
    assert result(test_boards[1], (0,0)) == test_boards[7]

test_player()
test_actions()
test_result()

print("tests passed")
