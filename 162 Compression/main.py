# http://www.reddit.com/r/dailyprogrammer/comments/25clki/5122014_challenge_162_easy_novel_compression_pt_1/
# http://www.reddit.com/r/dailyprogrammer/comments/25hlo9/5142014_challenge_162_intermediate_novel/
# http://www.reddit.com/r/dailyprogrammer/comments/25o2bd/5162014_challenge_162_hard_novel_compression_pt_3/

import argparse
import re


def compress(input_filepath):
    with open(input_filepath, 'r') as input_file:
        text = input_file.read()
    dictionary = []
    compressed_text = ''

    lower = re.compile(r'[a-z]+')
    upper = re.compile(r'[A-Z]+')
    capitalised = re.compile(r'[A-Z][a-z]*')

    tokens = re.split(r'(\W)', text)
    for token in tokens:
        if token in ['', ' ']:
            pass
        elif token == '\n':
            compressed_text += 'R '
        elif token in '.,?!;:':
            compressed_text += token + ' '
        elif token == '-':
            compressed_text += '- '
        elif lower.fullmatch(token):
            if token not in dictionary:
                dictionary.append(token)
            compressed_text += str(dictionary.index(token)) + ' '
        elif upper.fullmatch(token):
            token = token.lower()
            if token not in dictionary:
                dictionary.append(token)
            compressed_text += str(dictionary.index(token)) + '! '
        elif capitalised.fullmatch(token):
            token = token.lower()
            if token not in dictionary:
                dictionary.append(token)
            compressed_text += str(dictionary.index(token)) + '^ '
        else:
            raise ValueError('Error! Token %s not handled.' % token)
    compressed_text += 'E'

    dictionary_output = str(len(dictionary)) + '\n' + '\n'.join(dictionary)
    return dictionary_output + '\n' + compressed_text


def decompress(input_filepath):
    with open(input_filepath, 'r') as input_file:
        wordcount = int(input_file.readline())
        dictionary = [input_file.readline().rstrip() for _ in range(wordcount)]
        compressed_text = input_file.readline()

    chunks = [chunk.replace(' ', '') for chunk in compressed_text.split(' ')]
    text = ''
    for chunk in chunks:
        if chunk == '-':
            if len(text) == 0 or text[-1] != ' ':
                text += '-'
            else:
                text = text[:-1] + '-'
        elif chunk in '.,?!;:' and len(chunk) == 1:
            if len(text) == 0 or text[-1] != ' ':
                text += chunk + ' '
            else:
                text = text[:-1] + chunk + ' '
        elif chunk.lower() == 'r':
            text += '\n'
        elif chunk.lower() == 'e':
            break
        elif chunk[-1] == '^':
            text += dictionary[int(chunk[:-1])].title() + ' '
        elif chunk[-1] == '!':
            text += dictionary[int(chunk[:-1])].upper() + ' '
        else:
            text += dictionary[int(chunk)].lower() + ' '
    return text


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('mode')
    argparser.add_argument('input_filepath')
    argparser.add_argument('output_filepath')
    args = argparser.parse_args()

    if args.mode == 'c':
        output = compress(args.input_filepath)
    elif args.mode == 'd':
        output = decompress(args.input_filepath)
    else:
        raise ValueError('Mode specifier must be c or d')

    with open(args.output_filepath, 'w') as output_file:
        output_file.write(output)