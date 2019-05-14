import random

a = random.randint(1, 9)
b = 0
print(a)



c = 0

while b != a:
  b = input ("What is your guess?")
  

  if b =="exit":
    break
  b = int(b)
  if b == a: 
    print ("That is correct!")
  else:
    print ("That is not correct")
  c = c+1
  print ("Number of guesses", c)
 
