# i created a Game in which Computer choose random number if u gues its number u winn else u lose(u have 5 lives!)
from random import random,randint
pcnumber = randint(1,10)
print("Correct answer: (if you choose it u won):",pcnumber,"\n")
lives = 0
tries = 1
while lives <= 4:
    
    print("life number:",tries)
    tries += 1
    user_choice = int(input("Welcome to 'GUES NUMBER' game!\nChoose a number from '1 to 10'\nIf you gues the number You won else You lose:"))
    if user_choice > pcnumber:
        print("Wrong answer ❌ ( Your number is High): ")
        lives += 1
    elif pcnumber + 2 >= user_choice:
        print("\nYou are too close: keep on trying!!\n")
        lives += 1
    elif pcnumber - 2 <= user_choice:
        print("\nYou are too close: keep on trying!!\n") 
        lives += 1

    elif user_choice < pcnumber:
         print("Wrong answer ❌ ( Your number is low): ")
         lives += 1
    elif user_choice == pcnumber:
        print("Congratulations You Won ✅ ! ")
        break
print("Game is over")
