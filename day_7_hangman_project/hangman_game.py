import random
from hangman_words import word_list
from hangman_art import stages, logo

end_of_game = False
chosen_word = word_list[random.randint(0, len(word_list) - 1)]
display = []
lives = 6
guess_letters = []

print(logo)
print(chosen_word)

for n in range(len(chosen_word)):
    display.append("_")

while not end_of_game:
    #Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()

    #validate if the user already try with the letter that he type.
    if guess in guess_letters:
        print(f"You already try with the letter {guess}")
    else:
        #Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
        guess_letters.append(guess)
        for n in range(len(chosen_word)):
            if guess == chosen_word[n]:
                display[n] = guess
        print(display)
        # if not in the chosen word, lose a live
        if guess not in chosen_word:
            lives -= 1
            #if it lose all the lives, it lose.
            if lives == 0:
                print("You Lose")
                end_of_game = True
        # if the user guess al the letters win.
        elif "_" not in display:
            print("You Win")
            end_of_game = True
        
        print(stages[lives])
