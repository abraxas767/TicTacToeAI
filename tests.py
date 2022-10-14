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

    [[X,O,_], # 8
     [O,X,_],
     [_,_,X]],

    [[X,O,X], # 9
     [X,O,_],
     [_,O,X]],

    [[X,O,X], # 10
     [X,O,_],
     [_,O,X]],

    [[X,O,X], # 11
     [_,O,_],
     [X,O,X]],

    [[O,O,X], # 12
     [_,X,_],
     [X,O,X]],
]

def test_player():
    assert player(test_boards[0]) == X
    assert player(test_boards[1]) == X
    assert player(test_boards[2]) == X
    assert player(test_boards[3]) == O
    assert player(test_boards[4]) == O
    assert player(test_boards[6]) == X

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

def test_utility():
    assert utility(test_boards[5]) == 1
    assert utility(test_boards[7]) == 0
    assert utility(test_boards[8]) == 1
    assert utility(test_boards[9]) == -1
    assert utility(test_boards[11]) == -1
    assert utility(test_boards[12]) == 1


test_player()
test_actions()
test_result()
test_utility()

print("tests passed")
