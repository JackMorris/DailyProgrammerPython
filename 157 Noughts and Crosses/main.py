# http://www.reddit.com/r/dailyprogrammer/comments/22fgs1/472014_challenge_157_easy_the_winning_move_xgames/

import copy


def row_solutions(grid, next_move):
    for row in range(3):
        if grid[row].count(next_move) == 2 and grid[row].count('-') == 1:
            col = grid[row].index('-')
            grid_copy = copy.deepcopy(grid)
            grid_copy[row][col] = next_move
            yield grid_copy


def column_solutions(grid, next_move):
    transposed_grid = [list(row) for row in zip(*grid)]
    for solution_grid in row_solutions(transposed_grid, next_move):
        yield [list(row) for row in zip(solution_grid)]


def diagonal_solutions(grid, next_move):
    for modifier in [0, 2]:
        # Use modifier to index through the two diagonals.
        diagonal = [grid[abs(0-modifier)][0],
                    grid[abs(1-modifier)][1],
                    grid[abs(2-modifier)][2]]
        if diagonal.count(next_move) == 2 and diagonal.count('-') == 1:
            index = diagonal.index('-')
            grid_copy = copy.deepcopy(grid)
            grid_copy[abs(index-modifier)][index] = next_move
            yield grid_copy


if __name__ == '__main__':
    next_move = input()
    grid = [list(input()) for _ in range(3)]
    solutions = []
    solutions += list(row_solutions(grid, next_move))
    solutions += list(column_solutions(grid, next_move))
    solutions += list(diagonal_solutions(grid, next_move))

    if len(solutions) == 0:
        print('No Winning Move')
    else:
        for solution_grid in solutions:
            print('\n'.join(''.join(row) for row in solution_grid), end='\n\n')