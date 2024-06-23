import random

# (a) Preprocessing: Create and shuffle the deck of cards
suits = ['SPADE', 'HEART', 'DIAMOND', 'CLUB']
ranks = ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']

deck = [(rank, suit) for suit in suits for rank in ranks]
random.shuffle(deck)

# (b) Settle the Stage: Deal the first two cards to player and dealer
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

# (c) Compute the Total Value
def get_hand_value(hand):
    total_value = 0
    num_aces = 0
    for card in hand:
        rank = card[0]
        if rank == 'ACE':
            num_aces += 1
            total_value += 11
        elif rank in ['JACK', 'QUEEN', 'KING']:
            total_value += 10
        else:
            total_value += int(rank)
    while total_value > 21 and num_aces > 0:
        total_value -= 10
        num_aces -= 1
    return total_value

player_total = get_hand_value(player_hand)
dealer_total = get_hand_value(dealer_hand)

# (d) Game Logic
player_busted = False
while not player_busted:
    print("Player's Hand:", player_hand, "Total Value:", player_total)
    decision = input("Do you want to hit (1) or stay (0)? ")
    if decision == '1':
        new_card = deck.pop()
        print("You drew:", new_card)
        player_hand.append(new_card)
        player_total = get_hand_value(player_hand)
        if player_total > 21:
            print("You busted!")
            player_busted = True
    else:
        break

dealer_busted = False
while dealer_total < 17:
    new_card = deck.pop()
    print("Dealer drew:", new_card)
    dealer_hand.append(new_card)
    dealer_total = get_hand_value(dealer_hand)
    if dealer_total > 21:
        print("Dealer busted!")
        dealer_busted = True
        break

# (e) Determine the Winner
if player_busted:
    print("Dealer wins!")
elif dealer_busted:
    print("Player wins!")
else:
    if player_total == dealer_total:
        print("It's a tie!")
    elif player_total > dealer_total:
        print("Player wins!")
    else:
        print("Dealer wins!")

# (f) Ask the Player to play again or quit
play_again = input("Do you want to play again? (yes/no): ")
if play_again.lower() == 'yes':
    # Reset the deck and hands
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    # Repeat the game logic...
else:
    print("Thanks for playing Blackjack!")
