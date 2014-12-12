# http://www.reddit.com/r/dailyprogrammer/comments/20sjif/4192014_challenge_154_intermediate_gorellian/

word_count, order = input().split(' ')
word_count, order = int(word_count), order.upper()

words = [input() for _ in range(word_count)]
words.sort(key=lambda s: [order.index(c) for c in s.upper()])
print('\n'.join(words))