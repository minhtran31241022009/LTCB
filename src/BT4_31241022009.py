# Complete the following requirements
# 1. making a report about: number of win/lose
# 2. assume that you have 100$. In each game, you should pay 5$.
# After finishing game, report the amount go got.
# 3. Game will end if you lost all money
import random
money = 100
win, lose = 0, 0
print(f"You have {money}$")
while True:
    print("Computer thinks a number from 1 to 100")
    comp_num = random.randint(1, 100)
    level = int(input("Choose the level [1-easy],[2-medium],[3-hard]: "))
    times = 10 if level == 1 else 5 if level == 2 else 3
    bet = int(input("Enter your bet: "))
    is_win = False
    for time in range(times):
        your_num = int(input("Enter your guessing number #"+str(time+1)+": "))
        if your_num == comp_num:
            is_win = True
        else:
            if your_num < comp_num:
                print("Too low!")
            else:
                print("Too high!")
        if is_win and time +1 <= times:
            print("You win!")
            win += 1
            money += bet
            print("----------------------------------")
            print(f"Your money is {money} now")
            break
        if time +1 >= times:
            print("You lose!")
            lose += 1
            money -= bet
            print("----------------------------------")
            print(f"Your money is {money} now")
    if money <= 0:
        print("You're out of money! Game over!")
        break
    cont = input("Do you want to play again? [y/n]: ").strip().lower()
    if cont == "n":
        break
print("----------------------------------")
print("Thank you for playing!")
print(f"Your money: {money}")
print(f"Your win: {win}")
print(f"Your lose: {lose}")