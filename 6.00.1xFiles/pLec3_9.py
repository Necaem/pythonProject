# lecture 3.9
# bisection guess of user input

guess = "g"
maxLimit = 100
minLimit = 0
avgLimit = (maxLimit + minLimit)/2
print "Please think of a number between 0 and 100!"
while guess != "c":
    print "Is your secret number " + str(avgLimit) + "?"
    print "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.",
    guess = raw_input("Enter 'c' to indicate I guessed correctly.")
    if guess == "h":
        maxLimit = avgLimit
        avgLimit = (maxLimit + minLimit)/2
    elif guess == "l":
        minLimit = avgLimit
        avgLimit = (maxLimit + minLimit)/2
    elif guess == "c":
        print "Game over. Your secret number was: " + str(avgLimit)
    else:
      print "Sorry, I did not understand your input." 
       
       
       
    

