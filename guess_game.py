import getpass
first_player = input("enter your name: ")
second_player = input("enter your name: ")
secret_number = getpass.getpass("enter your secret number:")
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess the number: "))
    guess_count += 1
    if guess == secret_number:
        print(f"{second_player} won!!")
        break
else:
    print(f"{first_player} won!!")
