"""
Python Crash Course: Function Exercises
12/06/18
"""

"""
Exercise 1
Create a function with the name hello
that prints "Hello, string", where string can be replaced by any string object. 
For instance, if string = "World!", the function should print "Hello, World!".
"""


#Test:
hello("World!")
hello("Jack")
hello("Jill")


""""
Exercise 2
Create a function with the name sentence
that takes a list of strings of the format [Name, age, activity] and prints
"Name is age years-old and likes activity". So the input ["Joe", "8", "drawing"]
should result in the output "Joe is 8 years-old and likes drawing."

Hint: In python, the index of the first element of a list is 0. The index of the 
second element of a list is 1. and so on...
"""


#Test
lstA = ["Joe", "8", "drawing"]
lstB = ["Sarah", "10", "soccer"]
sentence(lstA)
sentence(lstB)


"""
Exercise 3
Create a function with the name adding that takes five numbers, adds them together,
and returns their sum. So if the input is 1,2,3,4,5, the function should return the
#value 15. 
"""


#Test
Sum1=adding(1,2,3,4,5)
print(Sum1)
Sum2=adding(3,6,9,10,1)
print(Sum2)

