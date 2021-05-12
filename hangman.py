
import random
name = input()
print(f"hey {name} Let's play Hangman")
file = open("hangmanwords.txt.txt","rt")
data = file.readline()
wordlist = data.split(",")
word = random.choice(wordlist)
word = word.lower()
print(word)
guesses = []
turns = 8
done = False
while not done:
    for char in word.lower():
        if char in guesses:
            print(char,end=" ")
        else:
            print("_",end = " ")
    print()
    guess = input(f"Guess a charcter, You still have {turns} chances to complete the word : ")
    guesses.append(guess)
    if guess not in word.lower():
        turns = turns - 1
        if turns == 0:
            print("You lost, You don't have enough chances to continue")
            break
    done = True
    for char in word.lower():
        if char not in guesses:
            done = False 
if done:
    print("you won,guessed the word perfectly")
else:
    print("U lost, Play Again!")
            
file.close()          
            
        
