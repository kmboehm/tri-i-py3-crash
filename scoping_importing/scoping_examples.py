#Scoping Examples
A = 0
Name = "bob"
def my_function(c):
   d = 3
   print(c) 
   print(d)
   return c,d



# print(my_function(7))
# print(A)
# print(Name)
# print(c)
# print(d)


def add1(x , y):
    print(x,y)
    return x+y

# ans = add1(2,3)
# print(ans)
# print(x,y)


def add2(x , y):
    z = x+y
    print(x,y,z)

# ans = add2(2,3)
# print(ans)
# print(x,y,z)



def add3(x , y):
    z = x+y
    print(x,y,z)
    return z

# ans = add3(2,3)
# print(ans)
# print(x,y,z)




x = 5
y = 6

def add(a,b):
   return a+b 

def update_x(a):
   global x	
   x += a
   return x

def test():
   if x>5:
      return "nice!"
   else:
      return "not yet"



print(test())

print(x,y)

print(add(x,3))

print(x,y)

print(add(x,y))
print(x,y)

print(update_x(y))
print(x,y)

print(test())

