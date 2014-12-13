# http://www.reddit.com/r/dailyprogrammer/comments/24r50l/552014_161_easy_blackjack/

import random


def get_shuffled_cards(n):
    """ Represent cards as (name, numerical_value) tuples. """
    values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
              'Jack', 'Queen', 'King']
    suits = ['♣', '♦', '♥', '♠']
    names = [value + ' ' + suit for suit in suits for value in values]
    numerical_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*4
    cards = list(zip(names, numerical_values))*n
    random.shuffle(cards)
    return cards


def get_game_stats(cards):
    hand_count = 0
    blackjack_hands = []
    while len(cards) > 1:
        hand_count += 1
        hand = [cards.pop(), cards.pop()]
        if sum(map(lambda c: c[1], hand)) < 12 and len(cards) > 0:
            hand.append(cards.pop())
        if sum(map(lambda c: c[1], hand)) == 21:
            blackjack_hands.append(hand)
    return hand_count, blackjack_hands


def print_status(hands, blackjack_hands):
    blackjack_count = len(blackjack_hands)
    percent_blackjacks = 100*(blackjack_count/hands)
    print('After %d hands there were %d blackjacks (%.0f%%)' %
          (hands, blackjack_count, percent_blackjacks))

    blackjack_hands = [map(lambda c: c[0], hand) for hand in blackjack_hands]
    blackjack_hands = [', '.join(hand) for hand in blackjack_hands]
    print('\n'.join(blackjack_hands))


if __name__ == '__main__':
    number_of_decks = int(input('Number of decks: '))
    shuffled_cards = get_shuffled_cards(number_of_decks)
    hand_count, blackjack_hands = get_game_stats(shuffled_cards)
    print_status(hand_count, blackjack_hands)