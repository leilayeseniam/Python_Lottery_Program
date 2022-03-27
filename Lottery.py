'''
    Author: Leila Yesenia Maisonet
    Date: 12/07/2020
    Purpose: Interactive program that sees if its numbers match the user's input to win money.
'''
import random

#Get user's name
userName = input ("Please enter your name:")

#Greet user and explain purpose of program
print ("Hello", userName, "Welcome to the Lottery Program! Let's see if you can win some money.")

#Ask the user to input a number from 0-9
userNumber1 = eval(input("Input a random number from 0 through 9: "))

#Ask the user to input a number from 10-39
userNumber2 = eval(input("Input a random number from 10 through 39: "))

#Ask the user to input a number from 40-99
userNumber3 = eval(input("Input a random number from 40 through 99: "))

#Ask the user to input an uppercase letter from A-Z
userLetter = ord(input("Input a random uppercase letter from A through Z: "))

#Program will generate a random number from 0-9
randomNumber1 = random.randint(0,9)

#Program will generate a random number from 10-39
randomNumber2 = random.randint(10,39)

#Program will generate a random number from 40-99
randomNumber3 = random.randint(40,99)

#Program will generate a random uppercase letter from A-Z
randomLetter = ord(chr(random.randint(65,90)))

#Print the User's numbers and letter and the Program's numbers and letter
print("User's lotto: ", userNumber1, ",", userNumber2, ",", userNumber3, ", and ", chr(userLetter), ".")
print("Program's winning lotto: ", randomNumber1, ",", randomNumber2, ",", randomNumber3, ", and ", chr(randomLetter), ".")

#Check whether there are matches
match3 = userNumber1 == randomNumber1 and userNumber2 == randomNumber2 and userNumber3 == randomNumber3
match2 = userNumber1 == randomNumber1 and userNumber2 == randomNumber2 or userNumber1 == randomNumber1 and userNumber3 == randomNumber3 or userNumber2 == randomNumber2 and userNumber3 == randomNumber3
match1 = userNumber1 == randomNumber1 or userNumber2 == randomNumber2 or userNumber3 == randomNumber3
matchL = userLetter == randomLetter

if match3 and matchL:
    print("You matched all 3 numbers and the letter! You won $5,095.")
    
elif match3:
    print("You matched all 3 numbers but not the letter! You won $5,000.")

elif match2 and matchL:
    print("You matched 2 numbers and the letter! You won $345.")

elif match2:
    print("You matched 2 numbers but not the letter! You won $250.")

elif match1 and matchL:
    print("You matched 1 number and the letter! You won $105.")

elif match1:
    print("You matched 1 numbers but not the letter! You won $10.")

elif matchL:
    print("You matched the letter but no numbers! You won $95.")

else:
    print("Sorry, no matches at all. Better luck next time")
 
