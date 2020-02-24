def main():
    print ("Hello, this is a guessing game guess an animal")
    animal = str("Pig")
    guess = input (str("The game is thinking of an animal take a guess:"))
    guess = guess.capitalize()
    while guess != "Pig":
        print ("Wrong Guess again")
        guess = input(str("Enter and animal:"))
    if guess == "Pig":
        print("You win")
main()

