#!/usr/bin/python3

import sys

with open('input.txt', 'r') as f:
#with open('test.txt', 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    moves = lines[0].split(',')
    lines.pop(0)
    boards = []
    board = []
    while lines:
        line = lines.pop(0)
        if not line:
            continue
        if len(board) == 5:
            boards.append(board)
            board = []
        board.append(line.split())
    if len(board) == 5:
        boards.append(board)

    def is_winner(board):
        print("board", board)
        for i in range(0, 5):
            print("row", board[i])
            if all(c == 'X' for c in board[i]):
                return True
            col = [board[j][i] for j in range(0, 5)]
            print("col", col)
            if all(c == 'X' for c in col):
                return True
        return False
    winner = None
    for move in moves:
        print("move", move)
        for board in boards:
            for i in range(0, 5):
                board[i] = [c if move != c else 'X' for c in board[i]]
            if len(boards) == 1 and is_winner(board):
                winner = board
                break
        if winner:
            break
        boards = [board for board in boards if not is_winner(board)]
        last_board = boards[0]
    
        print("boards", boards)
        print("len", len(boards))
    print("WINNER:", winner)
    winner = last_board
    v = sum([int(winner[i][j]) if winner[i][j] != 'X' else 0 
             for i in range(0, 5) 
             for j in range(0, 5)])
    print("last move", move)
    print(v)
    print(v*int(move))

