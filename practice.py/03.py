import random

# Datetime module


'''
Add 10 days to the current data.
'''

# now_date = datetime.datetime(2025, 6, 27, 4, 56)
# ten_days_from_now = now_date + datetime.timedelta(days=10)
# print(ten_days_from_now)


'''
Subtract 3 hours and 45 minutes from the current time.
'''

# now_time = datetime.timedelta(hours=5, minutes=44)
# sub_time = now_time - datetime.timedelta(hours=3, minutes=45)
# print(sub_time)


# Random module


'''
Question 2. Dice Game Simulation
Simulate a dice game where:

Two players roll a 6-sided dice 5 times each.

Print each player's rolls.

Display the winner (player with the highest total), or say it's a draw.

✨ Hint: Use random.randint(1, 6) in a loop.
'''

player_1_lst = []
player_2_lst = []

for i in range(1, 6):

    player_1_lst.append(random.randint(1, 6))
for i in range(1, 6):
    player_2_lst.append(random.randint(1, 6))

print(f"Player 1 rolls: {player_1_lst}")
print(f"Player 2 rolls: {player_2_lst}")

if sum(player_1_lst) > sum(player_2_lst):
    print(f"Player 1 got the highest point {sum(player_1_lst)} ----> Player 1 is the winner of the game!!!")
elif sum(player_2_lst) > sum(player_1_lst):
    print(f"Player 2 got the highest point {sum(player_2_lst)} ----> Player 2 is the winner of the game!!!")
elif sum(player_1_lst) == sum(player_2_lst):
    print(f"{sum(player_1_lst)} == {sum(player_2_lst)} --> It's a draw!!!")


# print(player_1)
