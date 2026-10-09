import random
import os

# ================= HANGMAN GAME =================


categories = {
    "Fruits": [
        "APPLE", "MANGO", "BANANA", "CHERRY",
        "ORANGE", "PAPAYA", "GRAPES", "PEACH"
    ],

    "Animals": [
        "LION", "TIGER", "ELEPHANT", "MONKEY",
        "RABBIT", "HORSE", "PANDA", "ZEBRA"
    ],

    "Programming": [
        "PYTHON", "COMPUTER", "KEYBOARD",
        "MONITOR", "PROGRAM", "INTERNET",
        "LAPTOP", "HANGMAN"
    ],

    "Countries": [
        "PAKISTAN", "INDIA", "CHINA",
        "CANADA", "TURKEY"
    ]
}


stages = [
"""
 +---+
 |   |
     |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========
"""
]


def load_high_score():

    if os.path.exists("highscore.txt"):

        file = open("highscore.txt", "r")

        score = file.read()

        file.close()

        return int(score)

    return 0



def save_high_score(score):

    file = open("highscore.txt", "w")

    file.write(str(score))

    file.close()



def choose_category():

    print("\nChoose Category:")

    keys = list(categories.keys())

    for i in range(len(keys)):

        print(i + 1, ".", keys[i])


    while True:

        choice = input("Enter choice: ")


        if choice.isdigit():

            choice = int(choice)

            if 1 <= choice <= len(keys):

                return keys[choice - 1]


        print("Invalid choice!")



def choose_difficulty():

    print("\nDifficulty")

    print("1. Easy")
    print("2. Medium")
    print("3. Hard")


    while True:

        d = input("Choose difficulty: ")


        if d in ["1","2","3"]:

            return d


        print("Invalid choice!")



def choose_word(category, difficulty):

    words = categories[category]


    if difficulty == "1":

        words = [w for w in words if len(w) <= 5]


    elif difficulty == "2":

        words = [w for w in words if 6 <= len(w) <= 7]


    else:

        words = [w for w in words if len(w) >= 8]


    if len(words) == 0:

        words = categories[category]


    return random.choice(words)



def give_hint(word, guessed):

    hidden = []

    for i in range(len(word)):

        if guessed[i] == "_":

            hidden.append(i)


    if hidden:

        index = random.choice(hidden)

        letter = word[index]


        for i in range(len(word)):

            if word[i] == letter:

                guessed[i] = letter


        return letter


    return None



# ================= GAME START =================


player = input("Enter your name: ")


high_score = load_high_score()


total_score = 0

wins = 0

losses = 0



while True:


    print("\n========================")

    print("      HANGMAN GAME")

    print("========================")


    category = choose_category()

    difficulty = choose_difficulty()


    word = choose_word(category, difficulty)


    guessed = ["_"] * len(word)

    guessed_letters = []


    wrong = 0

    score = 100

    hint_used = False



    while wrong < 6 and "_" in guessed:


        print(stages[wrong])


        print("Category:", category)

        print("Word:", " ".join(guessed))

        print("Score:", score)

        print("Used:", guessed_letters)


        guess = input("\nEnter letter (H for hint): ").upper()



        if guess == "H":


            if hint_used:

                print("Hint already used!")

                continue


            hint = give_hint(word, guessed)

            hint_used = True

            score -= 5


            print("Hint:", hint)

            continue



        if len(guess) != 1 or not guess.isalpha():

            print("Enter only one letter!")

            continue



        if guess in guessed_letters:

            print("Already guessed!")

            continue



        guessed_letters.append(guess)



        if guess in word:


            for i in range(len(word)):

                if word[i] == guess:

                    guessed[i] = guess


            print("Correct!")


        else:

            wrong += 1

            score -= 10

            print("Wrong!")




    if "_" not in guessed:


        print("\n🎉 YOU WON 🎉")

        print("Word:", word)

        wins += 1

        total_score += score


    else:


        print(stages[wrong])

        print("\nGAME OVER")

        print("Word was:", word)

        losses += 1




    if total_score > high_score:

        high_score = total_score

        save_high_score(high_score)



    print("\n========= REPORT =========")

    print("Player:", player)

    print("Wins:", wins)

    print("Losses:", losses)

    print("Total Score:", total_score)

    print("High Score:", high_score)



    again = input("\nPlay Again? (Y/N): ").upper()


    if again == "N":

        print("\nThanks for playing", player)

        break