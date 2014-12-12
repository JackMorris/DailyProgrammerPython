# http://www.reddit.com/r/dailyprogrammer/comments/217klv/4242014_challenge_154_easy_march_madness_brackets/

from re import sub, findall

string, current_level = input(), 0
required_levels = len(findall('[\[{\(]', string)) + 1
levels = ['']*required_levels

for c in string:
    if c in '[{(':
        current_level += 1
    elif c in ']})':
        current_level -= 1
    else:
        levels[current_level] += c

# Remove excess spaces.
levels = [sub(' +', ' ', s.lstrip().rstrip()) for s in levels]

# Print the deepest level first.
for level in reversed(levels):
    print(level, end=' ')