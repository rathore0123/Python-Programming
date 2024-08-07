import random
i = 0
point = 0
while(i!=7):
    user = input("Enter your choice 'S' for snake 'W' for water 'G' for gun or to 'quit' please type exit: ")
    if(user == 'quit'):
        break
    ls = ['S','W','G']
    index = random.randint(0,len(ls)-1)
    bot = ls[index]
    if(user == bot):
        print(f"No one wins! your choice is {user} and bot choice is also {bot}")
    elif(user == 'S' and bot == 'W'):
        print(f"Congratulations You won a point!  your choice is {user} and bot choice is {bot}")
        point += 1
    elif(user == 'S' and bot == 'G'):
        print(f"Better Luck next time!  your choice is {user} and bot choice is {bot}")
    elif(user == 'W' and bot == 'G'):
        print(f"Congratulations You won a point!  your choice is {user} and bot choice is {bot}")
        point += 1
    elif(user == 'W' and bot == 'S'):
        print(f"Better Luck next time!  your choice is {user} and bot choice is {bot}")
    elif(user == 'G' and bot == 'S'):
        print(f"Congratulations You won a point!  your choice is {user} and bot choice is {bot}")
        point += 1
    elif(user == 'G' and bot == 'W'):
        print(f"Better Luck next time!  your choice is {user} and bot choice is {bot}")
    else:
        print("Please Enter a valid choice")

    i += 1

print(f"You have earned {point} Points")