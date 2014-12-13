# http://www.reddit.com/r/dailyprogrammer/comments/236va2/4162014_challenge_158_intermediate_part_1_the/

description_string = input()
lines, max_len = [], 0
i = 0

while i < len(description_string):
    whitespace_count = 0
    if description_string[i] in '123456789':
        whitespace_count = int(description_string[i])
        i += 1
    line_string = ' '*whitespace_count
    line_string += '++--***...'[:(ord(description_string[i]) - 96)]
    lines.append(line_string)
    max_len = max(max_len, len(line_string))
    i += 1

# Pad lines to same length.
lines = [line + ' '*(max_len - len(line)) for line in lines]

for row in range(max_len):
    print(''.join(line[max_len - row - 1] for line in lines))