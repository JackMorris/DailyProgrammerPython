# http://www.reddit.com/r/dailyprogrammer/comments/1givnn/061713_challenge_130_easy_roll_the_dies/

from random import randint

while True:
    rolls, faces = input().split('d')
    for _ in range(int(rolls)):
        roll_result = randint(1, int(faces))
        print(roll_result, end=' ')
    print()