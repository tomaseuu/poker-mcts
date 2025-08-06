# win_estimator.py


import random
from mcts import Node
from card_utils import create_deck, shuffle_deck, draw_cards
from evaluator import compare_hands


def run_mcts(my_hand, num_simulations):
    root = Node(state= {"my_hand": my_hand})

    for i in range(num_simulations):
        node = root

        while node.children and node.fully_expanded():
            node = node.select_best_child()

        if not node.fully_expanded():
            game_state = generate_random_poker_state(my_hand)
            node = node.add_child(game_state)

        result = game_result(node.state)

        node.backpropagate(result)
    return root.wins / root.visits

# create and shuffle deck
def generate_random_poker_state(my_hand):
    deck = create_deck()
    shuffle_deck(deck)

    for card in my_hand:
        deck.remove(card)

    opponent_hand = draw_cards(deck, 2)

    # Sample the Community Cards
    flop = draw_cards(deck, 3)
    turn = draw_cards(deck, 1)
    river = draw_cards(deck, 1)

    return {
        "my_hand": my_hand,
        "opponent_hand": opponent_hand,
        "community": flop + turn + river
    }

# Full Poker Game state and determines who wins
def game_result(game_state):
    my_hand = game_state["my_hand"] + game_state["community"]
    opponent_hand = game_state["opponent_hand"] + game_state["community"]
    
    result = compare_hands(my_hand, opponent_hand)

    if result == 1:
        return "Win!"
    elif result == -1:
        return "Loss!"
    else:
        return "Tie!"
    
def estimate_win_rate(my_hand, simulations=10000):
    win_rate = run_mcts(my_hand, simulations)
    return win_rate * 100 
