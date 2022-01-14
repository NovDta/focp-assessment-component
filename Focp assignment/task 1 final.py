print("Stop! Who would cross the Bridge of Death\nMust answer me these questions three, 'ere the other side he see.")

question_1 = input('What is your name? ')  # Input name from user
question_1 = question_1.upper()  # Capitalize input string

if "ARTHUR" in question_1:  # If King passes, access is granted without further questions
    print('My liege! You may pass!')
else:
    # If Knight passes, he is asked further questions
    question_2 = input('What do you seek? ')
    question_2 = question_2.upper()  # Input is capitalized

    if "GRAIL" not in question_2:  # If it isn't "The Grail" the Knight seeks, he is denied access
        print('Only those who seek the Grail may pass!')
    else:
        # If the Knight does not know his favourite colour, he has to face the Gorge of Eternal Peril
        question_3 = input('What is your favourite color? ')
        question_3 = question_3.upper()  # Input is capitalized

        # Knight's favourite colour must start with the first letter of his name
        if question_3[0] == question_1[0]:
            # If answer is correct, he is allowed to pass
            print('You may pass!')
        else:
            print('Incorrect! You must now face the Gorge of Eternal Peril')
