"""
For Python Crash Course: 12/6/16
Slide Code for the Functions Section

"""

#Parameters and Return Statements
def add_noreturn(x , y):
    z = x+y
    print(z)

add_noreturn(2,3)

def add(x , y):
    return x+y

z = add(2,3)
print(z)




#Order of the parameters matters:
def subtract(x , y):
    return x-y
    
ans = subtract(2,3)
print(ans)

ans = subtract(3,2)
print(ans)




#Required and optional parameters:
def add(x , y = 2):
    return x+y

ans = add(2,3)
print(ans)

ans = add(2)
print(ans)




#Comments:
"""
This is a comment
"""
#print(5)
print(3) #This is a comment.



#An example of commenting a function:

def my_mean(num_lst):
    """
    Calculates the mean of a list of numbers.
    Input:
       num_lst = a list of numbers (type int or float)
                 of at least length 1
    Output:
       my_mean = the average of the elements in num_lst
    """
    sum_lst = 0
    count = 0
    #cycle through the elements of num_lst collecting the
    #sum over all elements and the number of elements
    for element in num_lst:
        sum_lst = sum_lst + element
        count = count + 1
    Mean = sum_lst/count
    return Mean

lstA = [1,2,4,6,8]
my_mean(lstA)



