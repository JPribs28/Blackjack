"""Base classes that can be used to create a card game.

Contains classes to create a card, make a deck of cards and
make players to interact with those cards.

"""

import random


class Card:

    def __init__(self, value, color):
        self.value = value
        self.color = color

    def display(self):
        print("[{}{}]".format(self.value, self.color), end=' ')

    def card_value(self):
        return self.value


class Deck:

    def __init__(self):
        self.deck = []
        self.new_deck()
        self.shuffle()
        self.shuffle()

    def new_deck(self):

        num_decks = 2

        # suits = ['\u2664', '\u2661', '\u2662', '\u2667']  # Unicode for outline suit symbols
        suits = ['\u2660', '\u2665', '\u2666', '\u2663']  # Unicode for solid suit symbols
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.deck = [Card(value, suit) for value in values * num_decks for suit in suits * num_decks]

    def display(self):
        for card in self.deck:
            card.display()

    def shuffle(self):
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop()


class Player:

    def __init__(self):
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def show_hand(self):
        for card in self.hand:
            card.display()

    def discard(self):
        return self.hand.pop()
