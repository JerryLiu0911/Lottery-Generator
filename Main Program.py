import random         #imports the random library
x = list(range(1,50)) #creates a list of numbers to choose from
num=[]                #generates list for the lottery numbers
for i in range(0,6) :
  num.insert(i,z:=random.choice(x))      #randomly picks 6 lottery numbers (non-repetitively)
  x.remove(z)
print (num)
print ("Bonus number :", bn:=random.choice(x))   #picks and prints the bonus number
