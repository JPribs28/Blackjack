import os
from card_game import Deck, Player


def calculate_hand(hand):
    """
    Calculates integer value of cards in player or dealer hand.

    :param hand: List of two or more cards
    :return: Total integer value of cards
    """

    # Separate aces from cards in hand. Aces have two potential values and need calculated differently
    # depending on current score

    non_aces = [c.card_value() for c in hand if c.card_value() != 'A']
    aces = [c.card_value() for c in hand if c.card_value() == 'A']

    total = 0

    for c in non_aces:  # Score all non ace cards in hand
        if c in 'JQK':
            total += 10
        else:
            total += int(c)

    for c in aces:  # Score all aces in hand.
        if total <= 10:
            total += 11
        else:
            total += 1

    return total


# Loop that runs to start a new hand.

while True:

    # Initialize and shuffle new deck.

    deck = Deck()
    deck.shuffle()

    # Initialize player and dealer then deals cards to them. Set values to determine if beginning of hand and if player
    # chose to stand or not.

    player = Player()
    dealer = Player()

    player.draw(deck)
    dealer.draw(deck)
    player.draw(deck)
    dealer.draw(deck)

    first_hand = True
    player_stand = False

    # Loop that runs while player is playing current hand. Once player stands the dealer will finish drawing cards as
    # needed, calculate hands and determine whether it was a win loss or draw for the player.

    while True:

        # Clears screen each time player makes a decision to give the appearance that the screen has been updated.

        os.system('cls' if os.name == 'nt' else 'clear')

        player_score = calculate_hand(player.hand)
        dealer_score = calculate_hand(dealer.hand)

        print('--------------BlackJack--------------\n')

        # Conditional to determine whether to display the dealer's second card or not based on game play decisions.

        dealer_blackjack = False

        if first_hand and dealer_score == 21:  # Checks if dealer has blackjack
            dealer_blackjack = True

        if player_stand or dealer_blackjack:  # Prints all cards in dealer hand.
            print('Dealer Cards: ', end=' ')
            for card in dealer.hand:
                card.display()
            print('  Score: ({})'.format(dealer_score))

        else:
            print('Dealer Cards: ', end=' ')  # Prints question marks for second dealer card if game is in progress.
            for card in dealer.hand:
                card.display()
                print('[??]')
                break

        # Prints cards in players hand.

        print('\nYour cards:', end=' ')
        for card in player.hand:
            card.display()

        print('  Score: ({})\n'.format(player_score))

        if player_score > 21:
            print('You busted!\n')
            input('Press ENTER to play again!')
            break

        if first_hand and player_score == 21:
            print('Blackjack! You win!\n')
            input('Press ENTER to play again!')
            break

        if first_hand and dealer_score == 21:
            print('Dealer has blackjack. You lose :(\n')
            input('Press ENTER to play again!')
            break

        first_hand = False

        # If player stands, compares scores to determine outcome of match. Prints appropriate results.

        if player_stand:
            if dealer_score > 21:
                print('Dealer busted, you win!')
            elif player_score == dealer_score:
                print('Push. This round is a draw.')
            elif player_score > dealer_score:
                print('You beat the dealer. You win!')
            else:
                print('You lose :(')

            print('')
            input('Press ENTER to play again!')
            break

        print('What would you like to do?')
        print(' [1] Hit')
        print(' [2] Stand')

        choice = input('\nYour choice: ')
        print('')

        if choice == '1':  # Add card from the deck to the player's hand.
            player.draw(deck)

        elif choice == '2':
            player_stand = True
            while calculate_hand(dealer.hand) <= 16:  # Deals cards to the dealer while the total is 16 or less.
                dealer.draw(deck)
