# ================ MORE ON LISTS =============================

# This the first time you might have seen an import statement. 
# See the Homework notes for more.
from task5 import list_of_booleans

# We already defined list_of_booleans in task5.py (we don't need the extension.py). Let's check that it works here

print("\n ======= task 6 ====== \n")

print("Our list of Booleans is", list_of_booleans, "\n")

# You might also note that when you run this Python file, all of the print statements from task5.py also execute.
# That's because in importing from this file, it also runs it. Right now, it should be a good way to compare the 
# variables in task5.py and our list_of_booleans we are importing here. If it annoys you, you can always go into
# task5.py and comment out all the print statements.

# Even though it is a list containing booleans, note that this variable is still of the type list
print("The variable type of list_of_booleans is", type(list_of_booleans), "\n")  

# Let's access an element of list_of_booleans using a defined index (i) - remember we start counting from zero (0). 
i = 3
element = list_of_booleans[i]

print(f"Element [{i}] of list_of_booleans is", element, "\n")

# You might notice that we have done something a bit fancy with the print statement above. We have turned formatting
# on by putting an f at the start, just before the first inverted comma. This allows us to use variable values in the
# string. We do this by placing the variable name in curly brackets ({}). In this case we want it to print the value 
# of our index, i. 

# We can see that it has the type Boolean
print(f"Element [{i}] of list_of_booleans has type", type(element), "\n")

# At this point, we will introduce another built-in function: len.
# Short for length, this function is used the same as type. It gives
# you a count of the number of elements in a list or similar variable. 

print(f"The variable list_of_booleans has {len(list_of_booleans)} elements.", "\n")

print(f"Therefore we can index this list between values of [0] and [{len(list_of_booleans)-1}].", "\n")

# Task 6.0: change the value if the index (i) to another value to access a different element of list_of_booleans.
# There should be a clue in the output of the last print statement as to what the range of value you can enter for
# the index without incurring a IndexError.


