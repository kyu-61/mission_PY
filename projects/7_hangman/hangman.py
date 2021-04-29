import random
from art import stages, logo
from wordlist import list_
from replit import clear


print(logo)
print()
sel_word = random.choice(list_)
dash = []
for d in sel_word:
    dash.append("_")
print(dash)
print()
end_ = False
lives = 6

while not end_:
    guess = input("Enter a letter : ")
    clear()    

    if guess in dash:
        print(f"You've already guessed the letter {guess}")
        lives -= 1
        
    for i in range(len(sel_word)):
        letter = sel_word[i]
        if guess == letter:
            dash[i] = letter  
    
    if guess not in sel_word:
        lives -= 1
        if lives == 0:
            end_ = True
            print("you lose")
            print(f"The answer is {sel_word}")
    
    print(dash)
    
    if "_" not in dash:
        end_ = True
        print()
        print("You win")
    
    print(stages[lives])
    
