# http://www.reddit.com/r/dailyprogrammer/comments/1pwl73/11413_challenge_139_easy_pangrams/

line_count = int(input())
lines = [input().upper() for _ in range(line_count)]

for line in lines:
    counts = [0]*26
    for c in line:
        c_index = ord(c) - ord('A')
        if 0 <= c_index < 26:
            counts[c_index] += 1

    is_pangram = all(count > 0 for count in counts)
    print(str(is_pangram), end='\t')
    for c_index in range(26):
        char = chr(c_index + ord('A'))
        print('%s:%d' % (char, counts[c_index]), end=' ')
    print()