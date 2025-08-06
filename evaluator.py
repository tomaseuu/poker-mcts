# evaluator.py

# Map ranks to numbers
def evaluate_hand(cards):
    rank_map = {'2': 2, '3': 3, '4': 4, '5': 5, 
                '6': 6, '7': 7, '8': 8, '9': 9, 
                'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
               }
    
    # Converting string cards to tuples (ex. (13, 'Hearts'))
    parsed_cards = []
    for card in cards:
        parts = card.split()
        rank = parts[0]
        suit = parts[1]
        rank_value = rank_map[rank]
        parsed_cards.append((rank_value, suit))

    # Checking to see how many times each card rank shows up
    rank_counts = {}
    for card in parsed_cards:
        rank = card[0]
        if rank in rank_counts:
            # if this rank has already been visited, add 1 to the count
            rank_counts[rank] += 1
        else: 
            # if it is the first time being visited, set count to 1
            rank_counts[rank] = 1

    # Checking to see how many times each card suit shows up
    suit_counts = {}
    for card in parsed_cards:
        suit = card[1]
        if suit in suit_counts:
            suit_counts[suit] += 1
        else:
            suit_counts[suit] = 1

    # Finds which suit has 5 or more cards, and stores it in flush_suit
    for suit in suit_counts:
        count = suit_counts[suit]
        if count >= 5:
            flush_suit = suit
            break
        else: 
            flush_suit = None

    # Grabs the number of times each card rank appears to make it easier
    counts = list(rank_counts.values())

    #straight_high function
    straight_high = find_straight(list(rank_counts.keys()))

    # Check to see if it is a Straight Flush or a Royal Flush
    if flush_suit:
        suited_ranks = []
        for card in parsed_cards:
            rank = card[0]
            suit = card[1]

            if suit == flush_suit:
                suited_ranks.append(rank)

        straight_flush_high = find_straight(suited_ranks)
        
        if straight_flush_high:
            if straight_flush_high == 14:
                print("You have a Royal Flush!")
                return (1, [14])
            else:
                print("You have a Straight Flush!")
                return (2, [straight_flush_high])


    # Four of a Kind
    if 4 in counts:
        print("You have four of a kind!")
        return (3, [find_highest_rank_with_count(rank_counts, 4)])
    
    # Full House
    elif 3 in counts and 2 in counts:
        print("You have a Full House!")
        return (4, [find_highest_rank_with_count(rank_counts, 3), find_highest_rank_with_count(rank_counts, 2)])

    # Flush - (Note: Reverse = True, looks at the highest/bestest cards first)
    elif flush_suit: 
        print("You have a Flush!")
        flush_cards = []
        for card in parsed_cards:
            rank = card[0]
            suit = card[1]
            if suit == flush_suit:
                flush_cards.append(rank)
        flush_cards.sort(reverse=True)
        return(5, flush_cards[:5])
    
    # Straight
    elif straight_high:
        print("You have a Straight!")
        return(6, [straight_high])
    
    # Three of a Kind
    elif 3 in counts:
        print("You have Three of a Kind!")
        return (7, [find_highest_rank_with_count(rank_counts, 3)])  

    # Two Pair
    elif counts.count(2) == 2:
        print("You have Two Pair!")
        return (8, get_ranks_by_count(rank_counts, 2))  

    # One Pair
    elif 2 in counts:
        print("You have One Pair!")
        return (9, [find_highest_rank_with_count(rank_counts, 2)])  

    # High Card
    else:
        print("You have High Card!")
        high_cards = sorted(rank_counts.keys(), reverse=True)
        return (10, high_cards[:5])  

# Function to remove duplicates, handle straights, find the highest straight,
# and returns the highest card in that straight
def find_straight(ranks):
    ranks = sorted(set(ranks)) # removes duplicates

    # Ace can act like 1
    if 14 in ranks:
        ranks.append(1)
    continuous= []      # current sequence of continuous numbers
    max_straight= []    # store longest straight it finds

    for rank in ranks:
        if continuous and rank == continuous[-1] + 1:
            continuous.append(rank)
        elif not continuous or rank != continuous[-1]:
            continuous = [rank]
        if len(continuous) >= 5:
            max_straight = continuous[:] # makes a copy
    if max_straight:
        return max_straight[-1]
    else:
        return None
    
# returns highest rank that appear exactly 'count' times
def find_highest_rank_with_count(rank_counts, count):
    for rank in sorted(rank_counts.keys(), reverse = True):
        if rank_counts[rank] == count:
            return rank
    return 0

# returns all ranks that appear exactly 'count' times 
def get_ranks_by_count(rank_counts, count):
    ranks = []
    for rank in sorted(rank_counts.keys(), reverse=True):
        if rank_counts[rank] == count:
            ranks.append(rank)
    return ranks

# Tie-Win-Lose Comparison
def compare_hands(hand1, hand2):
    eval_1 = evaluate_hand(hand1)
    eval_2 = evaluate_hand(hand2)

    rank_1 = eval_1[0]
    rank_2 = eval_2[0]

    # lower rank is better!
    if rank_1 < rank_2:
        # win
        return 1
    elif rank_1 > rank_2:
        # lose
        return -1
    else:
        tie_breaker_1 = eval_1[1]
        tie_breaker_2 = eval_2[1]

    # Comparing Tie-Breakers one by one
    i = 0
    while i < len (tie_breaker_1) and i < len(tie_breaker_2):
        if tie_breaker_1[i] > tie_breaker_2[i]:
            return 1
        elif tie_breaker_1[i] < tie_breaker_2[i]:
            return -1
        else: 
            i += 1
    return 0
