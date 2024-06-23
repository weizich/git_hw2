import random

def initialize_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def deal_card(deck, player_hands, player):
    card = deck.pop()
    if player not in player_hands:
        player_hands[player] = []
    player_hands[player].append(card)

def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card, suit in hand:
        if card in ['J', 'Q', 'K']:
            value += 10
        elif card == 'A':
            num_aces += 1
            value += 11
        else:
            value += int(card)
    
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    
    return value

# Example usage:
deck = initialize_deck()
player_hands = {}

deal_card(deck, player_hands, 'Player 1')
deal_card(deck, player_hands, 'Player 1')
deal_card(deck, player_hands, 'Player 2')
deal_card(deck, player_hands, 'Player 2')

print("Player 1's hand:", player_hands['Player 1'], "Value:", calculate_hand_value(player_hands['Player 1']))
print("Player 2's hand:", player_hands['Player 2'], "Value:", calculate_hand_value(player_hands['Player 2']))
