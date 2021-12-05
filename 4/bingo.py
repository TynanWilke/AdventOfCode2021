#!/usr/bin/python3

import sys

with open('input.txt', 'r') as f:
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
        diag1 = [board[i][i] for i in range(0, 5)]
        print("diag1", diag1)
        if all(c == 'X' for c in diag1):
            return True
        diag2 = [board[4-i][4-i] for i in range(0, 5)]
        print("diag2", diag2)
        if all(c == 'X' for c in diag2):
            return True
        return False
    winner = None
    for move in moves:
        print("move", move)
        for board in boards:
            for i in range(0, 5):
                board[i] = [c if move != c else 'X' for c in board[i]]
            if is_winner(board):
                winner = board
                break
        if winner:
            break
    print("WINNER:", winner)
    v = sum([int(board[i][j]) if board[i][j] != 'X' else 0 
             for i in range(0, 5) 
             for j in range(0, 5)])
    print(v)
    print(v*int(move))

