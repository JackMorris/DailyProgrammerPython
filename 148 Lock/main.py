# http://www.reddit.com/r/dailyprogrammer/comments/1v4cjd/011314_challenge_148_easy_combination_lock/

N, c1, c2, c3 = input().split()
N, c1, c2, c3 = int(N), int(c1), int(c2), int(c3)

spins = 2*N             # Spin two times clockwise
spins += c1             # Spin to first number clockwise
spins += N              # Spin one time counter-clockwise
spins += (c1-c2) % N    # Spin to second number counter-clockwise
spins += (c3-c2) % N    # Spin to third number clockwise
print(spins)