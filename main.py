import random
import hangman_words
import hangman_art
lives = 6
win = 1

end_game = False
guessed = 0

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
print(hangman_art.stages[lives])
# print(chosen_word)
guess = str(input("Guess a letter!\n").lower())
ok_guess = 0

if guess >= 'A' and guess <= 'z':
    ok_guess = 1

while ok_guess == 0:
    if ok_guess == 0:
        guess = str(input("Guess a letter!\n").lower())
        if guess >= 'A' and guess <= 'z':
            ok_guess = 1

placeholder = []
for letter in chosen_word:
    placeholder.append("_")

print(''.join(placeholder))

ok = 0
for i in range(0, len(chosen_word)):
    if chosen_word[i] == guess:
        placeholder[i] = guess
        ok += 1
        guessed = 1

if guessed == 0:
    lives -= 1

# print(ok)
print(''.join(placeholder))
print(hangman_art.stages[lives])

while end_game == 0:
    while ok < len(placeholder) and lives > 0:
        guessed = 0
        guess = str(input("Guess a letter!\n").lower())
        ok_guess = 0

        if guess >= 'A' and guess <= 'z':
            ok_guess = 1

        while ok_guess == 0:
            if ok_guess == 0:
                guess = str(input("Guess a letter!\n").lower())
                if guess >= 'A' and guess <= 'z':
                    ok_guess = 1

        for i in range(0, len(chosen_word)):
            if chosen_word[i] == guess:
                placeholder[i] = guess
                ok += 1
                guessed = 1

        if guessed == 0:
            lives -= 1

        print(hangman_art.stages[lives])
        # print(placeholder)
        print(''.join(placeholder))

    if ok == len(placeholder):
        end_game = True
        win = 1

    if lives <= 0:
        end_game = True
        win = 0

if win == 1:
    print("You won!\n")
else:
    print("You lost!")
    print(f"The word was: {chosen_word}\n")