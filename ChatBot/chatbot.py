from datetime import date

BOT_NAME = "CHARLIE"
CURRENT_YEAR = date.today().year

if __name__ == "__main__":
    # stage 1
    print(f"Hello! My name is {BOT_NAME}\nI was created in {CURRENT_YEAR}") 

    # stage 2
    print("Please, remind me your name.")
    username = input()
    print(f"What a great name you have, {username}!")

    #  stage 3
    print(("Let me guess your age."
          "\nEnter remainders of dividing your age by 3, 5 and 7."))

    remainders = [int(input()) for _ in range(3)]  # Ask for remainders

    remainder3, remainder5, remainder7 = remainders
    user_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

    print(f"Your age is {user_age}; that's a good time to start programming!")

    #  stage 4
    print("Now I will prove to you that I can count to any number you want.")

    number_count = int(input())
    for i in range(number_count+1):
        print(f"{i}!")

    print("Completed, have a nice day!")
