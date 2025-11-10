import random

def request_words_list():
    words_list = []
    words_quantity = int(input("\nEnter the number of words (mín 10): "))
    print()
    
    while words_quantity < 10:
        words_quantity = int(input("Less than needed! Please enter a different value. (mín 10): "))
    
    for i in range (words_quantity):
        words_list.append(input(f"Enter the {i+1}° word: "))   

    return words_list


def draw_word(words_list):
    list_size = len(words_list)
    drawn_index = random.randint(0, list_size-1)
    drawn_word = words_list[drawn_index]

    return drawn_word


def scramble_word(drawn_word):
    characters = []
    for i in drawn_word:
        characters.append(i)

    n = len(characters)

    total_shuffles = 2 * n -1
    counter = 0

    while counter < total_shuffles:
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)

        if i != j:
            sup = characters[i]
            characters[i] = characters[j]
            characters[j] = sup
            counter += 1
        else:
            continue

    scrambled_word = ""
    for letter in characters:
        scrambled_word += letter

    return scrambled_word


def jogar(drawn_word, scrambled_word):
    total_attempts = 7
    current_attempt = 1

    print(f"\nThe scrambled word is: {scrambled_word}")
    print("You have 7 attempts. Good Luck!\n")

    while current_attempt <= total_attempts:
        guess = input(f"Attempt {current_attempt}/{total_attempts} -> Enter your guess: ").strip()

        if guess.lower() == drawn_word.lower():
            print("\n🏆 Congratulations! You guessed the word correctly!")
            return True
        else:
            print("Wrong word! Try again. \n")
            current_attempt += 1

    return False

print("======= Scrambled Word Game =======")

words_list = request_words_list()
drawn_word = draw_word(words_list)
scrambled_word = scramble_word(drawn_word)
ganhou = jogar(drawn_word, scrambled_word)

if not ganhou:
    print("\n☠️  GAME OVER! You didn't get the word right.")
    print(f"The word was: {drawn_word}")