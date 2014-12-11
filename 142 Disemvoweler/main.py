# http://www.reddit.com/r/dailyprogrammer/comments/1ystvb/022414_challenge_149_easy_disemvoweler/

input_string = input().replace(' ', '')
vowels = 'aeiou'
print(''.join(c for c in input_string if c not in vowels))
print(''.join(c for c in input_string if c in vowels))