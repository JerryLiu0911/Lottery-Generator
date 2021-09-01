import random
import math                   #imported math library for math calculations
ticket=False                  #a variable that will act as a flag for the validity of the user's lottery ticket
x = list(range(1,50))
r=49
y=6                           #defined variables that will be used for calculating percentage
k=43
n=0
num=[]
for i in range(0,6) :
  num.insert(i,z:=random.choice(x))
  x.remove(z)
bn=random.choice(x)
num.append(bn)                           #appended the bonus number into the list to allow the program to compare all the numbers.
while ticket != True :                   #while loop so the user can re-enter their ticket
  if len(t:=input("input your 6 digit lottery ticket seperated by spaces.").split()) != 6:                  #creates a list consisting of the user's lottery ticket numbers while checking to see if all 6 numbers are inputted.
    print("You can only have 6 numbers on your lottery ticket. Please reenter your lottery ticket.")        
  else:
    ticket=True
    for lottery_numbers in range(6):
      t[lottery_numbers]=int(t[lottery_numbers])                             #converting each element in the list to an integer
      if t[lottery_numbers] > 49 or t[lottery_numbers] < 1:
        print(t[lottery_numbers], "is not a valid number.Please reenter your lottery ticket.")    #checking if the numbers entered are valid
        ticket=False
        continue
    for n1 in range(0,6):                                                                         #checking for repeated numbers
      for n2 in range(1+n1,6):
        if t[n1]==t[n2] and n1 != n2:
            print ("There should not be any repeating numbers.Please reenter your lottery ticket.")
            ticket=False
            break
      if ticket==False:
        break
    if ticket == True:                                       #outputs the user's lottery ticket for final confirmation if entered correctly
      print(t)
      if c:=input("Do you confirm this is your lottery ticket?(enter 'yes' or 'no')") == "yes":
          ticket=True
      else:
        ticket=False
for numbers in t:                                             #comparing numbers on lottery ticket to lottery numbers, outputting the correct ones.
  for l in num:
    if numbers==l:
      print("you got number",numbers,"correct.")
      n+=1                                                    #records number of lottery numbers correct for calculating probability of combination
num.remove(bn)
p=((math.factorial(6)/(math.factorial(n)*math.factorial(6-n)))*(math.factorial(43)/(math.factorial(6-n)*math.factorial(43-(6-n)))))/((math.factorial(49)/(math.factorial(6)*math.factorial(49-6))))
print("The probability of you getting this combination is",p )
print("The lottery number was ",num)                              #displays calculated probabiity and lottery numbers
print("Bonus number :", bn)
