def quiz_game():
    import random
    # Welcome to the quiz game! 
    print("Welcome to the quiz game!")

    # categories of quiz topics
    categories = ["Computers", "Animals", "History"]
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
        if category.capitalize() not in categories:
            print("Sorry, invalid input")
            continue
        else:
            break

    #importing and storing the questions of the chosen category
    cat_chosen = __import__(category)
    questions = cat_chosen.questions
    library = cat_chosen.question_library

    # The game code
    while playing.lower() == "y":
        #initialization
        print(f"Best of luck on five trivia questions on {category.capitalize()}!")
        score = 0
        i = 5
        questions_ask = []
        #questions
        for num in range(i):
            question_num = random.randint(0,len(questions)-1)
            while question_num in questions_ask:
                question_num = random.randint(0,len(questions)-1)
            print(questions[question_num])
            answer = input("Answer: ")
            if library[questions[question_num]] == answer.capitalize():
                print("Great Job!")
                score += 1
                print(f"Your score is {score}")
            else:
                print(f"Sorry, wrong answer, the correct answer is {library[questions[question_num]]}")
            questions_ask.append(question_num)
            print(questions_ask)

        
        while True:
            playing = input("would you like to play again? (y/n) ")
            if not playing.lower() == "y" and not playing.lower() == "n":
                print("Sorry, invalid input")
                continue
            else:
                break
        print("Thank you for playing!")


quiz_game()