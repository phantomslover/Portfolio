import random

print("""Welcome to the Number Guessing Game! 
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number. \n""")

print("""Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)""")

choice = int(input("Enter your choice: "))
print()
if choice == 1:
    chances = 10
    print("Great! You have selected the Easy difficulty level.")
elif choice == 2:
    chances = 5
    print("Great! You have selected the Medium difficulty level.")
elif choice == 3:
    chances = 3
    print("Great! You have selected the Hard difficulty level.")

print("Let's start the game!")

attempts = 0
rand_num = random.randrange(1, 101)
while chances > 0:
   guess = int(input("Enter your guess: "))
   if rand_num > guess:
       attempts += 1
       chances -= 1
       print(f"Incorrect! The number is greater than {guess}.")
       print()
   elif rand_num < guess:
       attempts += 1
       chances -= 1
       print(f"Incorrect! The number is less than {guess}.")
       print()
   else:
       break

if chances == 0:
    print("You lose!")
else:
    print(f"Congratulations! You guessed the correct number in {attempts} attempts.")