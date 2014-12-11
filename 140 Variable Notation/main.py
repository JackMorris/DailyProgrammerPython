# http://www.reddit.com/r/dailyprogrammer/comments/1q6pq5/11413_challenge_140_easy_variable_notation/

CAMEL_CASE, SNAKE_CASE, UPPER_SNAKE_CASE = 0, 1, 2


def convert_to_mode(string, mode):
    """ Convert `string` to the format specified by `mode`. """
    if mode == CAMEL_CASE:
        return string[0].lower() + string.title().replace(' ', '')[1:]
    if mode == SNAKE_CASE:
        return string.lower().replace(' ', '_')
    if mode == UPPER_SNAKE_CASE:
        return string.upper().replace(' ', '_')


def convert_from_mode(string, mode):
    """
    Convert `string` from the format specified by `mode` to lowercase space
    delimited words.
    """
    if mode == CAMEL_CASE:
        uppercase_indices = [0]
        for (i, c) in enumerate(string):
            if 'A' <= c <= 'Z':
                uppercase_indices.append(i)
        uppercase_indices.append(len(string))

        words = []
        for i in range(1, len(uppercase_indices)):
            words.append(string[uppercase_indices[i-1]:uppercase_indices[i]])
        return ' '.join(words).lower()

    if mode == SNAKE_CASE or mode == UPPER_SNAKE_CASE:
        return string.replace('_', ' ').lower()


if __name__ == '__main__':
    from_mode, to_mode = input().split()
    input_string = input()

    plain = convert_from_mode(input_string, int(from_mode))
    print(convert_to_mode(plain, int(to_mode)))


