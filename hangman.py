import random
words = ["enum", "colab", "python", "game", "vscode"]

word= random.choice(words)
guessed_letters = []
attempt = 6

print("welcome to hangman game project 8")
print(" _ " * len(word))

while attempt > 0:
    guess = input("\n Guess the Letter:").lower()

    if len(guess) != 1 or not guess.isalpha():
       print("write one alphabate only!")
       continue
    if  guess in guessed_letters:
        print("This letter is already chosen")
        continue
    guessed_letters.append(guess)

    if guess in word:
        print("correct guess!")
    else:
        attempt -= 1  
        print(f"wrong {attempt} attempts.")  

    displayed_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])   
    print(displayed_word)

    if "_" not in displayed_word:
        print(f"Congragulations you have guessed: {word}")
        break
else: 
    print(f"Game Over! the correct word is: {word}" )