import random 

hello = "Tashi Delek,"
game = input(hello + " wanna play the roll dice game?\n")
if game == "yes": 
    print("let's start the game") 
    count = 1
# run loop till count is less than 5
    while count < 100:
        count = count + 1
        roll = random.randint(1,6)
        guess = int(input("Guess the dice roll:\n"))
        if guess == roll:
            print("yay! you guessed it right, it was " + str(roll))
        elif guess > 6:
            print("end game!") 
            break
        else: 
            print("Dommage! you guessed it wrong, it was " + str(roll))
else:
    input("good bye, enjoy your day!")
