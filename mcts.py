# mcts.py

import math
import random


exploration_c = math.sqrt(2)

# initializes a new node with game state, win count, etc
class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.wins = 0
        self.visits = 0

    # Checks if added 1000 child possibilities alraedy
    def fully_expanded(self):
        return len(self.children) >= 1000
    
    # Adds a new child node to explore a new possibility 
    def add_child(self, child_state):
        child_node = Node(child_state, parent=self)
        self.children.append(child_node)
        return child_node
    
    # Upper Confidence Bound to help decide which node to explore during MCTS
    def ucb1(self):
        if self.visits == 0:
            return float('inf') # infinity
        exploitation = self.wins / self.visits
        exploration = exploration_c * math.sqrt(math.log(self.parent.visits) / self.visits)
        return exploitation + exploration
    
    # Selects the child with the highest UCB1 value
    def select_best_child(self):
        return max(self.children, key=lambda child: child.ucb1())
    
    # update win/visit counts going up the tree (back up again)
    # it is to help the algorithm "learn" which choices led to wins
    def backpropagate(self, result):
        node = self
        while node is not None:
            node.visits += 1
            if result == "Win!":
                node.wins += 1
            elif result == "Tie!":
                node.wins += 0.5
            node = node.parent


