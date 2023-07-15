
import random

top_of_range = int(input("Type a number: "))
random_number = random.randint(0,top_of_range)
guesses = 0
while True:
    user_guess = input("Make a guss:")
    guesses+=1
#this code is to check is user given value is int or not?

    if user_guess.isdigit():       #here we're using  -----------. isdigit()  function
       user_guess = int(user_guess)
    else:
        print("pls type a number next time.")
        continue

    if user_guess == random_number:
        print("YOu got it!-------------------")
        break

    elif user_guess > random_number:
        print("You were above the number!")

    else:
        print("You were below the number!")

print("YOu got it in" , guesses, "guesses; ")





