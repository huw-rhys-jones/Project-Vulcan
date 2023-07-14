print(" ")

# ========================= Integers ====================#
# Integers are just whole numbers. You can use them for a 
# number of mathematical operations as shown below.

number_first = 9

number_second = 2

# you can check the type of any variable with the built-in type() function
print("The variable type of number_first is", type(number_first))

print("The variable type of number_first is", type(number_first))


# The above should tell you that number_first is of class 'int'
# don't worry about what a class is just yet, just focus on the 
# fact that it is an 'int' or integer type 

# Summation - the sum of two int variables is another int
integer_sum = number_first + number_second

print("The sum of the two numbers is:", integer_sum)
print("The variable type of integer_sum is", type(integer_sum))

print(" ")

# Multiplication - note that the multiple of two numbers is called the product 

integer_product = number_first * number_second

print("The product of the two numbers is:", integer_product)
print("The variable type of integer_product is", type(integer_product))

print(" ")

# Division - note that what you get from dividing two numbers is called the quotient 

integer_quotient = number_first / number_second

print("The quotient of the two numbers is:", integer_quotient)
print("The variable type of integer_quotient is", type(integer_quotient))

print(" ")

# What do you notice about integer_quotient that's different to all the rest? 
# We are have created a variable of a new type 

# You can also get the remainder of division between two numbers
integer_quotient_remainder = number_first % number_second
print("The remainder of division of the two numbers is:", integer_quotient_remainder)
print("The variable type of integer_quotient_remainder is", type(integer_quotient_remainder))

print(" ")
# ========================= Floats ====================#
# Floats, or floating point numbers, are numbers which have decimal places.

float_first = 1.345
print("The variable type of float_first is", type(float_first))

print(" ")

float_second = 0.0
print("The variable type of float_second is", type(float_second))

print(" ")

float_third = 0.354
print("The variable type of float_third is", type(float_third))

print(" ")

# A note on style: have you noticed something about the way I always name variables?
# It is good practice to name variables in snake_case that is all lower case with 
# underscores (_) between words. It isn't mandatory to do this, but it is strongly
# encouraged. It makes it far easier to read and debug.

# It is also good practice in variable naming to put the major subject first in the name
# for example, 'float' in the last three variables, then the secondary subject, such as 
# first/second/third.

# If we want to be really pedantic, most of the 'variables' I have defined above
# should actually be called constants i.e. they are given a value which never changes.
# Strictly speaking, constant names should be ALL_CAPS. They are usually defined right
# at the start of the Python file and then are only used, never redefined.

# On the subject of variables, this is probably obvious to you but they are called 
# such because they can change (or vary). They can be redefined at any time.
# Note the examples below.

variable_first = 3

print("The value of variable_first is", variable_first)

variable_first = 4

print("The value of variable_first is", variable_first)

print(" ")

# We can even reference the variable in its own redefinition:

variable_second = 5

print("The value of variable_second is", variable_second)

variable_second = variable_second + 1

print("The value of variable_second is", variable_second)

print(" ")

# ================ YOUR TASK 1 ===========================
# perform some mathematical operations using floats just 
# as we did for integers. You can use the floats I defined 
# previously or create your own. Try to do addition, 
# multiplication and division as well as self referencing.
# You could also try mixing up integers and floats and checking 
# the type.

float_sum = float_first + float_third

print("The sum of the two numbers is:", float_sum)

float_sum = float_first + float_second

print("The sum of the two numbers is:", float_sum)

float_product = float_first * float_third

print("The product of the two numbers is:", float_product)
print("The variable type of float_product is", type(float_product))

float_quotient = float_first / float_third

print("The quotient of the two numbers is:", float_quotient)
print("The variable type of float_quotient is", type(float_quotient))

float_sum = float_first + number_first

print("The sum of the two numbers is:", float_sum)

float_quotient = float_first / number_first

print("The quotient of the two numbers is:", float_quotient)
print("The variable type of float_quotient is", type(float_quotient))