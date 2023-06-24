# ========================= Strings ====================#
# Strings are just a series of ordinary characters. We can do 
# a series of operations on them just like with floats and ints.

# Summing strings
words_first = "These are not words "

print("The variable type of words_first is", type(words_first))

words_second = "and so are these "

words_summed = words_first + words_second

print(words_summed)

# Note that this isn't strictly summation at all. We are infact
# sticking something onto the end of something else, not summing
# their values. This process is referred to as concatenation. 

print(" ")

# Strings multiplied
words_multiplied = words_summed * 3

print(words_multiplied)

print(" ")
# The new line (\n)
# Here's something very useful, if you want to add a new line in a string, simply place the 
# characters backslash n (\n) in it

words_summed_newline = words_summed + "\n"
words_summed_newline_multiplied = words_summed_newline * 3

print(words_summed_newline_multiplied)

print(" ")

# ================ YOUR TASK 2 ===========================
# What about summing a string and an integer or float? You task is 
# to write code below to do that. 







# When you have attempted this, go back to the GitHub issue for this assignment and read the note.

# ========================================================





