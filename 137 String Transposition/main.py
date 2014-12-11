# http://www.reddit.com/r/dailyprogrammer/comments/1m1jam/081313_challenge_137_easy_string_transposition/

line_count = int(input())
lines = [input() for i in range(line_count)]
max_length = max(len(l) for l in lines)

# Pad lines so that they're all the same length.
lines = [l + ' '*(max_length-len(l)) for l in lines]

for row in range(max_length):
    row_characters = [lines[col][row] for col in range(line_count)]
    print(''.join(row_characters))