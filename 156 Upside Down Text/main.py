# http://www.reddit.com/r/dailyprogrammer/comments/226zqp/4042014_challenge_156_hard_u%CA%8Dop_%C7%9Dp%E1%B4%89sd_%C6%83u%E1%B4%89%C9%A5%CA%87%C7%9D%C9%AFos/

TEXT = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !.,'?0123456789"
UPSIDE_DOWN = "ɐqɔpǝɟƃɥıɾʞןɯuodbɹsʇnʌʍxʎzɐqɔpǝɟƃɥıɾʞןɯuodbɹsʇnʌʍxʎz ¡˙,,¿0123456789"
MAPPING = dict(zip(TEXT, UPSIDE_DOWN))

line_count = int(input())
lines = [input() for _ in range(line_count)]
for line in reversed(lines):
    print(''.join(MAPPING[c] for c in reversed(line)))