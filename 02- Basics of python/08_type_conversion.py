from traceback import print_tb


x = 10              # integer
y = 10.5            # float
z = "Hello"         # string
print(type(x)) 
print(type(y))
print(type(z))  
# implicit type conversion
# between float and int priority is for float
x = x * y
print(type(x))

# Explicit type conversion
age = input("What is your age? ")
age = int(age)
print(type(age))