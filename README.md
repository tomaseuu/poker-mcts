# Poker Win Estimator with Monte Carlo Tree Search (MCTS)

This project estimates the **pre-flop win probability** in Texas Hold'em poker using **Monte Carlo Tree Search (MCTS)** and the **UCB1** algorithm. It should simulate thousands of poker games to see how likely your hand is to win against one random opponent.

---

## How It Works

- You choose **2 hole cards** (which is your hand).
- The program:
  1. Randomly deals opponent cards and 5 community cards.
  2. Plays out the hand to the end (no folding, always to showdown).
  3. Repeats this thousands of times.
  4. Uses **MCTS** to learn which situations lead to wins.
- In the end, it should print your **estimated win rate** based on the simulations. The more simulations you have, the more accurate it becomes I believe.

---

## 📂 File Guide

| `main.py` | Run this to test your hand and print the win rate. You can edit your cards and number of simulations here. |

| `win_estimator.py` | Coordinates MCTS, generates random poker states, runs simulations, and returns win probability. |

| `mcts.py` | Implements the MCTS Node class and selection/backpropagation logic using UCB1. |

| `evaluator.py` | Evaluates poker hands (e.g., pairs, flushes, full house, etc.) and compares two 7-card hands. |

| `card_utils.py` | Builds a shuffled 52-card deck and handles drawing cards without duplicates. |

---

## 🧪 How to Use

1. Open `main.py`
2. Find these lines:

```python
my_hand = ['J Hearts', 'Q Spades']  # <-- Edit this to try different hands
simulations = 5000                  # <-- You can increase this for more accuracy
```
