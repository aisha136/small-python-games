from random import randint

#Ask user to input the maximum range number for the random number to be in.
top_of_range = input("Please input the maximum number (for the range) the guess can be in: ")

#boolean var
correct_input = False

#This while loop checks whether the user inputted an actual number greater than 0.
#The user will keep being prompted to enter a number greater than 0 (if they didn't do so initially).
while correct_input == False:
    if top_of_range.isdigit():
        if int(top_of_range) > 0:
            correct_input = True
    else:
        top_of_range = input("Please enter in an actual number greater than 0: ")

#Create the random number (for guessing) by using the randrange() method.
number_to_guess = randint(0, int(top_of_range))

#user_guess var is for collecting the user's guess and comparing it to the number_to_guess.
#tries var is for collecting the amount of times the user has tried to guess the correct number.
user_guess = 0
tries = 0

#This while loop evaluates whether the number the user has guessed is equal to the random number (i.e. the number_to_guess).
#It also calculates the number of tries the user has guessed.
while number_to_guess != int(user_guess):
    tries += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == number_to_guess:
            print("You got it!")
            break
        elif user_guess > number_to_guess:
            print("Your guess is higher.")
        else:
            print("Your guess is lower.")

    else:
        print("Please enter a number next time.")
        user_guess = 0
        continue

#Print out the number of tries
print(f"You guessed it in {tries} tries.")
