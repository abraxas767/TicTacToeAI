def vv(arr):
    print(all([x is None for x in arr[k]] for k,v in enumerate(arr)))


x = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

y = [
    [None, None, None],
    [None, None, None],
    [None, 1, None]
]



def actions(board):

    final = set()

    for key, val in enumerate(sum(board, [])):
        if val == None:
            r = ((int(key/3),key % 3))
            final.add(r)

    print(final)


actions(y)
