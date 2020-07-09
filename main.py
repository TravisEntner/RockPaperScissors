import random
userChoice = input("Chose rock, paper, or scissors.")
choices = random.choice(['scissors', 'rock', 'paper'])
if(userChoice == "rock" and choices == 'scissors'):
 print("YOU WON, you chose " + userChoice + " The computer chose " + choices + ".")
elif(userChoice == "paper" and choices == 'rock'):
   print("YOU WON, you chose " + userChoice + " The computer chose " + choices + ".")
elif(userChoice == "scissors" and choices == 'paper'):
   print("YOU WON, you chose " + userChoice + " The computer chose " + choices + ".")
elif(userChoice == "rock" and choices == 'paper'):
   print("Oh No you lost, You chose " + userChoice + " the computer chose " + choices)
elif(userChoice == "paper" and choices == 'scissors'):
   print("Oh No you lost, You chose " + userChoice + " the computer chose " + choices)
elif(userChoice == "scissors" and choices == "rock"):
   print("Oh No you lost, You chose " + userChoice + " the computer chose " + choices)
elif(userChoice == "scissors" and choices == "scissors"):
  print("TIE")
elif(userChoice == "rock" and choices == "rock"):
  print("TIE")
elif(userChoice == "papaer" and choices=="paper"):
  print("TIE")
else:
   print("Please put rock, paper, or scissors. Also don't use capital letters") 
