import random

def roll_dice():
    dice_number = random.randint(1, 6)
    return dice_number

print("===== Welcome To Dice Rolling Simulator =====")
while 1:
    choice = input("Do you wanna roll a dice (yes/no): ")
    if 'yes' in choice.lower():
        print("Rolling dice...")
        number = roll_dice()
        print("Dice has the number:", number)
    elif 'no' in choice.lower():
        print('Exiting...')
        break
    else:
        print("Invalid input...please try again")