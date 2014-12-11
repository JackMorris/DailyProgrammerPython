# http://www.reddit.com/r/dailyprogrammer/comments/1qwkdz/111113_challenge_141_easy_checksums/

line_count = int(input())
lines = []
for i in range(line_count):
    lines.append(input())
for (i, line) in enumerate(lines):
    sum1, sum2 = 0, 0
    for c in line:
        sum1 = (sum1 + ord(c)) % 255
        sum2 = (sum2 + sum1) % 255
    print("%d %04X" % (i+1, sum1 | sum2 << 8))