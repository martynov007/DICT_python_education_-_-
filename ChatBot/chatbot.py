from datetime import date

BOT_NAME = "CHARLIE"
CURRENT_YEAR = date.today().year

if __name__ == "__main__":
    print(f"Hello! My name is {BOT_NAME}\nI was created in {CURRENT_YEAR}")
    print("Please, remind me your name.")
    username = input()
    print(f"What a great name you have, {username}!")
