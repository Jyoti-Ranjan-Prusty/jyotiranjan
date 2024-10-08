import time

def set_countdown():
    seconds = int(input("Enter amount of seconds: "))
    print('Countdown starts now...')
    temp = seconds
    while (temp != 0):
        if (temp != seconds):
            print('\b'*len(str(temp)), end='')
        time.sleep(1)
        temp -= 1
        print(temp, end='')
    print("\nCountdown ended...\n")

print("===== Welcome To Countdown Timer =====")
while True:
    choice = input("Do you want to set a countdown (yes/no): ")
    if 'yes' in choice.lower():
        set_countdown()
    elif 'no' in choice.lower():
        print('Exiting...')
        break
    else:
        print('Invalid input...please try again')