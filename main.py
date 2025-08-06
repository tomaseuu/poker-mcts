# main.py


from win_estimator import estimate_win_rate


my_hand = ['J Hearts', 'Q Spades'] 

simulations = 5000   # increase if you want better accuracy
estimated = estimate_win_rate(my_hand, simulations=simulations)

print("\n--------------------------------------")
print(f"Hand: {my_hand}")
print(f"Simulations: {simulations}")
print(f"Estimated Win Rate: {estimated:.2f}%")
print("--------------------------------------")
