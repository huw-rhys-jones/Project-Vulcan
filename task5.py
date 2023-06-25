# ================ BOOLEANS =============================


print(" ")


# ========== Directly defining booleans ============== #

boolean_defined_first = True
boolean_defined_second = False

print(boolean_defined_first, boolean_defined_second, "\n")

# You should see <class 'bool'> which is just short for Boolean
print("The variable type of boolean_defined_first is", type(boolean_defined_first), "\n")


# ========== Logical definition: Greater than
# Four is greater than 3 (True) and 2 isn't greater than
# 3 (False).

boolean_greater_first = 4 > 3
boolean_greater_second = 2 > 3

print(boolean_greater_first, boolean_greater_second, "\n")


# ========== Logical definition: less than
# Task 5.0: uncomment the following two lines and complete the 
# definition of each variable using the greater than (>) operator
# One should be True, one should be False. Print it out to check.

# boolean_less_first =  
# boolean_less_second = 

# print(boolean_less_than_first, boolean_less_than_second, "\n")


# ========== Logical definition: greater than or equal to
# Note that you are not restricted to only integers when making
# logical comparisons. You can even mix them up in the same
# operation.
 
boolean_greater_equal_first = 4.0 >= 4 
boolean_greater_equal_second = 2 >= 3.3

print(boolean_greater_equal_first, boolean_greater_equal_second, "\n")


# ========== Logical definition: less than or equal to
# Task 5.1: similar to task 5.0, uncomment the following two lines and
# complete the definition using the less than or equal to (<=) operator.
# Again, one should be True and the other False.

# boolean_less_than_equal_first = 
# boolean_less_than_equal_second = 

# print(boolean_less_than_equal_first, boolean_less_than_equal_second, "\n")


# ========== Logical definition: equal to
# Note that boolean comparisons don't even need to be numbers. Here we are 
# comparing two strings. Beer is Beer (True), but in this case, Resistance
# isn't Futile (False).

boolean_equal_first = "Beer" == "Beer"
boolean_equal_second = "Resistance" == "Futile"

print(boolean_equal_first, boolean_equal_second, "\n")


# ========== Logical definition: not equal to
# Task 5.2: you can problably guess what I am going to ask you to do here.
# Define two new variables with the boolean type that use the not equal to
# comparison (!=). Again, one should be True and one should be False. How
# you do this is entirely up to you.



# ========== Booleans in a list =============
# Lets now put all the booleans we have into a list. This will make it easier
# for us to access and use them later. I've started doing this for you below.
# Once you have completed the earlier tasks, you can uncomment lines 82 & 84
# and add your own variables on line 87.

list_of_booleans = [boolean_defined_first, boolean_defined_second, 
                    boolean_greater_first, boolean_greater_second,
                    # boolean_less_first, boolean_less_second, 
                    boolean_greater_equal_first, boolean_greater_equal_second,
                    # boolean_less_than_equal_first, boolean_less_than_equal_second,
                    boolean_equal_first, boolean_equal_second,
                    # Put your booleans from Task 5.2 here 
                    ]