#LIST COMPREHENSION VERY IMPORTANT
#https://www.practicepython.org/solution/2014/04/16/10-list-overlap-comprehensions-solutions.html


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#this was the solution using list comprehension in one line of code that instructs to create a new list with the duplicates included. 

result = [i for i in a if i in b]

print (result)
