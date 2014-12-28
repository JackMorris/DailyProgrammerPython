# http://www.reddit.com/r/dailyprogrammer/comments/2qmz12/20141228_challenge_195_easy_symbolic_link/

import re

link_count, links = int(input()), {}
for _ in range(link_count):
    link_path, target_path = input().split(':')
    links[link_path.rstrip('/')] = target_path.rstrip('/')

path = input().rstrip('/')

replacement_made = True
while replacement_made:
    replacement_made = False
    for link_path in links:
        if re.match(link_path, path):
            target_path = links[link_path]
            path = re.sub(link_path, target_path, path)
            replacement_made = True
            break

print(path)