# Either adding a tab or newline using escape sequences

# Using Tab
print("\tPython")

# Using Newline
print("This is a list example: \n1. Item 1 \n2. Item 2 \n3. Item 3")

# Removing whitespace with .strip(), .rstrip(), and lstrip():

# The .strip() method can be used to strip whitespace FROM BOTH SIDES.
favorite_language1 = "    Python    "
print(favorite_language1.strip())

# The .rstrip() method can be used to strip whitespace FROM THE RIGHT.
favorite_language2 = "Python     "
print(favorite_language.rstrip())

# The .lstrip() method can be used to strip whitespace FROM THE LEFT.
favorite_language3 = "     Python"
print(favorite_language2.lstrip())