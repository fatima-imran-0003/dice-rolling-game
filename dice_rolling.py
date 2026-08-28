#ask the user to roll the dice 
#if user enters y
    #generate the 2 random numbers 
    #print them
#elif user enter n 
    #print Thank you message 
    #Terminate the loop 
#else
    #print invalid number 

#need to import the libraries 
import random

while True:
    choice = input("Enter the number to roll the dice? (y/n): ").lower()

    if choice == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f'({dice1}, {dice2})')
    elif choice == 'n':
        print('Thanks for playing!')
        break
    else:
        print('Invalid choice!')
