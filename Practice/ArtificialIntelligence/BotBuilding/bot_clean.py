# https://www.hackerrank.com/challenges/botclean


def next_move(posr, posc, board):
    if board[posr][posc] == 'd':
        print("CLEAN")
        return
    layer = 1
    while True:
        if posc - layer >= 0 and board[posr][posc - layer] == 'd':
            print("LEFT")
            return
        if posc + layer < 5 and board[posr][posc + layer] == 'd':
            print("RIGHT")
            return
        if posr - layer >= 0 and board[posr - layer][posc] == 'd':
            print("UP")
            return
        if posr + layer < 5 and board[posr + layer][posc] == 'd':
            print("DOWN")
            return
        for i in range(1, layer):
            j = layer - i
            if posr - i >= 0 and (
                (posc - j >= 0 and board[posr - i][posc - j] == 'd') or
                (posc + j < 5 and board[posr - i][posc + j] == 'd')):
                print("UP")
                return
            if posr + i < 5 and (
                (posc - j >= 0 and board[posr + i][posc - j] == 'd') or
                (posc + j < 5 and board[posr + i][posc + j] == 'd')):
                print("DOWN")
                return
        layer += 1


import sys
if __name__ == "__main__":
    sys.stdin = open('in.txt', 'r')
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
