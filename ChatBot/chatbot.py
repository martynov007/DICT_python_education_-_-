from datetime import date

BOT_NAME = "CHARLIE"
CURRENT_YEAR = date.today().year

if __name__ == "__main__":
    print(f"Hello! My name is {BOT_NAME}\nI was created in {CURRENT_YEAR}")

    print("Please, remind me your name.")
    username = input()
    print(f"What a great name you have, {username}!")

    print(("Let me guess your age."
          "\nEnter remainders of dividing your age by 3, 5 and 7."))

    remainders = [int(input()) for inp in range(3)]  # Ask for remainders

    remainder3, remainder5, remainder7 = remainders
    user_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

    print(f"Your age is {user_age}; that's a good time to start programming!")
