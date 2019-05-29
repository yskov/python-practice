
#https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

x= input ("Insert a number? ")

x= int(x)

y = range (1, x+1)

z = list()

for i in y:
  if x%i == 0:
    z.append(i)
    


print (z)

#the above code is mine, but the below code is a way faster implementation: 

num = int(input("choose a number: "))
x = list(range(1, num+1))
print([i for i in x if num % i == 0])
