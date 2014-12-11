# http://www.reddit.com/r/dailyprogrammer/comments/1rdtky/111113_challenge_142_easy_falling_sand/

board_size = int(input())
board = []
for _ in range(board_size):
    board.append(list(input()))

changes_made = True
while changes_made:
    changes_made = False
    for row in range(board_size-1):
        for col in range(board_size):
            if board[row][col] == '.' and board[row+1][col] == ' ':
                changes_made = True
                board[row][col] = ' '
                board[row+1][col] = '.'

for row in board:
    print(''.join(row))