print("*************Welcome to the Basic Python Quiz*************")

#  Check if the user wants to play the game or not
userInput = input("Do you want to Play game (Yes/No)")

if userInput.lower() != "yes":
    quit()

print("Okay Lets Play !!!")
score = 0

question1 = input("What is the Full form of ONGC?\n")

if question1.lower() == "oil and natural gas corporation":
    score += 1
else :
    print("Incorrect")

question2 = input("What is the capital of Haryana?\n")

if question2.lower() == "chandigarh":
    score += 1
else :
    print("Incorrect")

print(f"Your score is {str(score)} !! Hurray")
print(f"Your Winning Percentage is {(score/2)*100}")
