# Command Line Blackjack

This is a simple Blackjack game that can be played in the commmand line.
The file `card_game.py` contains a class to create a card object, a class to
make a deck from those cards and a class to create a player that can interact
with those cards. The file `blackjack.py` contains the main logic for the
blackjack game using the classes provided.

In the `new_deck` method of the `Deck` class, there are two lines that
declare the variable `suits`. These are the unicode values used to represent
the suits of the playing cards (solid or outline). Currently, the one being used
is for solid symbols and can be easily switched by uncommenting whichever you
prefer. Also, the variable `num_decks` can be changed to desired number of decks
needed to be used in different card games.

