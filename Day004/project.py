rock = '''
                       888      
                       888      
                       888      
888d888 .d88b.  .d8888b888  888 
888P"  d88""88bd88P"   888 .88P 
888    888  888888     888888K  
888    Y88..88PY88b.   888 "88b 
888     "Y88P"  "Y8888P888  888
'''
paper = '''
88888b.  8888b. 88888b.  .d88b. 888d888 
888 "88b    "88b888 "88bd8P  Y8b888P"   
888  888.d888888888  88888888888888     
888 d88P888  888888 d88PY8b.    888     
88888P" "Y88888888888P"  "Y8888 888     
888             888                     
888             888                     
888             888
'''
scissors = '''
   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.
'''
import random
print("Welcome to Rock, Paper, Scissors!")
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
if user_choice == "0":
  print(rock)
elif user_choice == "1":
  print(paper)
elif user_choice == "2":
  print(scissors)
else:
  print("Invalid input. You lose!")
  exit()
print("Computer chose:")
computer_choice = random.randint(0, 2)
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
else:
  print(scissors)
if user_choice == str(computer_choice):
  print("It's a draw!")
elif user_choice == "0" and computer_choice == 2:
  print("You win!")
elif user_choice == "1" and computer_choice == 0:
  print("You win!")
elif user_choice == "2" and computer_choice == 1:
  print("You win!")
else:
  print("You lose!")