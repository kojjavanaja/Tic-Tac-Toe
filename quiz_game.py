print("Welcome my computer quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :")
score = 0

answer = input("What does CPU Stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Do you know DSA? ")
if answer.lower() == "Yes, I know DSA":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Do you know? ")
if answer.lower() == "yes, Iknow this topic":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input(" who are you? ")
if answer.lower() == "I'm a vanaja":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + "question correct")
print("You got " + str((score / 4) * 100) + "%.")