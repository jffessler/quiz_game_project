def quiz_game():
    # Welcome to the quiz game! 
    print("Welcome to the quiz game!")

    # categories of quiz topics
    categories = ["computers", "animals", "history"]
    #while loops for error handling the choices of whether to play and the category to play
    while True:
        playing = input("Would you like to play a game? (Y/N) ")
        if playing.lower() == "n":
            return print("Maybe next time!")
        elif playing.lower() != "y":
            print("Sorry, invalid input")
            continue
        else:
            break
    while playing.lower() == "y":
        category = input("Choose your category: computers, animals, or history: ")
        if category not in categories:
            print("Sorry, invalid input")
            continue
        else:
            break

    #importing the questions of the chosen category
    cat_chosen = __import__(category)
    print(cat_chosen.questions)

    # The game code
    while playing.lower() == "y":
        print("Best of luck!")

        while True:
            playing = input("would you like to play again? (y/n) ")
            if not playing.lower() == "y" and not playing.lower() == "n":
                print("Sorry, invalid input")
                continue
            else:
                break
        print("Thank you for playing!")


quiz_game()