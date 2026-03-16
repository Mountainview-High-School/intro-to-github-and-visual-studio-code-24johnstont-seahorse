import time
E1=input("Would you like your responses to be E-mailed?  (Y/N)").upper()
print("Welcome to the questionnaire")
questions = [0,1,2,3,4,5,6]
question=0
if question ==0:
  time.sleep(1)
Q0=input("Please enter your name")
question=1
if question ==1:
  time.sleep(1)
  Q1=input("Please enter your E-mail")
question=2
if question == 2:
 time.sleep(2)
Q2=input("What's your favourite colour?")
print("Awesome!")
question=3
if question==3:
   time.sleep(2)
Q3=input("What do you like to eat?")
print("That's pretty cool")
question=4
if question==4:
  time.sleep(2)
<<<<<<< Updated upstream
answer=input("What do you do for fun?")
=======
Q4=input("What do you do for fun?")
>>>>>>> Stashed changes
print("That's nice")
question=5
if question==5:
  time.sleep(2)
<<<<<<< Updated upstream
answer=input("Do you like sports?")
=======
Q5=input("Do you like sports?")
>>>>>>> Stashed changes
print("Okay")
question=6
if question==6:
  time.sleep(2)
<<<<<<< Updated upstream
answer=input("What's your favorite type of weather")
print("That's pretty cool")
  
=======
Q6=input("What's your favorite type of weather")
print("That's pretty cool")
results=7
if results==7:
 time.sleep(2)
 R1=input("Do you wnat to see your results? (Y/N)").upper()
while not (R1 == "Y" or R1 == "N"):
  print("You can't do that")
  time.sleep(2)
  R1=input("Do you wnat to see your results? (Y/N)").upper()
if R1 == "N":
  print("Thank you for taking this questionnaire")
elif R1 == "Y":
  print("Fetching your results")
  time.sleep(2)
  print(Q0,Q1,Q2,Q3,Q4,Q5,Q6)
  time.sleep(2)
  print("Thank you for taking this questionnaire")                                                                                                                                                                                                                                                                                                                                                                                                                                                              
if E1 == "Y":
>>>>>>> Stashed changes


 
 
 
 
 