# Variables are containers for a Value (string, integer, float, boolean). We assign values to variables using the `=` operator.
# a variable behaves as it was the value it contains (If you store a string it will be a string, if it was an integer it would act as an integer)

first_name = "Aashish"

print(first_name)

# print("first_name") 
# similarly with the earlier print statements, what happens if we try to enclose the variable in double or single quotes? Try it yourself and find the explanation at the end of file

# In order to print something along with the variable we have 2 different ways.

print("Welcome " + first_name + "!") # we simply print a welcome with space followed by first_name variable and then an exclamatory mark. There's a clean way.


# f-strings

# formatted-strings or f-strings allow you to dynamically pass variable values in string. (It can be numbers, strings, float, or boolean values)
# We use f'' or f"" to write a string and add curly braces to insert any particular variable.

print(f'Welcome {first_name}')



# Data Types

# Strings - A character or a series of characters (Words, sentences, paragraphs)

name = "John" #str

# Integers - whole numbers

rank = 1 #int

# Float - a decimal point value

gpa = 6.9 # float

# Boolean - A True or False Flag

is_american = False


# We can use all the values in a formatted string

print(f"Let's congratulate {name} on his {rank}st and {gpa}/7 gpa. The statement that 'John is American' is a {is_american} statement") 
# Note - If you have a single quotation in your f-string then the f string should be declared using double quotes and vice versa.