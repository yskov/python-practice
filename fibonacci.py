def fibonacci(x):
  

  

  count = 0
  r = 1

  c = [1]
  while count< x:
    
    r = c[count-1]+c[count]
    count = count +1 
    c.append(r)
    
  return (c)
