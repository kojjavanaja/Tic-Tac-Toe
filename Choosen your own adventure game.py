name = input("Type your name: ")
print("Welcome",name, "to this adcenture!")

answer = input("you are on a dirt road, it has come to an end and you can go left or right.which way would you like to go? ").lower()

if answer == "left":
    answer = input("you come to a river, you can walk around it or swim accross? ").lower()
    
    if answer == "swim":
        print("you swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("you walked for many miles, ran out of water and you lost the game")
    else:
        print('Not a valid option.you lose.')

elif answer == "right":
     print()
else:
    print('Not a valid option. you lose.')
