# http://www.reddit.com/r/dailyprogrammer/comments/1qdw40/111113_challenge_141_easy_monty_hall_simulation/

import random

wins = [0, 0]
run_count = int(input())

for _ in range(run_count):
    car_location = random.randint(0, 2)
    choice = random.randint(0, 2)
    winning_tactic = 0 if choice == car_location else 1
    wins[winning_tactic] += 1
print('Tactic 1: {:.1f}%'.format(100*wins[0]/run_count))
print('Tactic 2: {:.1f}%'.format(100*wins[1]/run_count))