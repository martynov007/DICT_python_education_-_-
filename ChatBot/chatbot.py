from datetime import date

BOT_NAME = "CHARLIE"
CURRENT_YEAR = date.today().year

if __name__ == "__main__":
    # stage 1
    print(f"Hello! My name is {BOT_NAME}\nI was created in {CURRENT_YEAR}")

    # stage 2
    print("\nPlease, remind me your name.")
    username = input()
    print(f"What a great name you have, {username}!")

    #  stage 3
    print(("\nLet me guess your age."
          "\nEnter remainders of dividing your age by 3, 5 and 7."))

    remainders = [int(input()) for _ in range(3)]  # Ask for remainders

    remainder3, remainder5, remainder7 = remainders
    user_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

    print(f"Your age is {user_age}; that's a good time to start programming!")

    #  stage 4
    print("\nNow I will prove to you that I can count to any number you want.")

    number_count = int(input())
    for i in range(number_count+1):
        print(f"{i}!")

    #  stage 5
    print("\nNow i'm gonna test your math skills!!!")
    print("What's the result of the expression 2 + 2 ?" +
          "\n1. 3\n2. 25\n3. i dunno :(\n4. 4")

    answer_variants = {
        1: "No, you'r wrong",
        2: "Too far to right answer",
        3: "Don't despair, secretly is 4",
        4: "Huurayy! You'r right"
    }
    while answer := int(input()):
        print(answer_variants.get(answer))

        if answer == 4:
            break

    print("Congratulations, have a nice day!")
