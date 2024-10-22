# Either adding a tab or newline using escape sequences

# 2.3.3.1
# Using Tab
print("\tPython")

# 2.3.3.2
# Using Newline
print("This is a list example: \n1. Item 1 \n2. Item 2 \n3. Item 3")

# Removing whitespace with .strip(), .rstrip(), and lstrip():

# 2.3.4.1
# The .strip() method can be used to strip whitespace FROM BOTH SIDES.
favorite_language1 = "    Python    "
print(favorite_language1.strip())

#2.3.4.2
# The .rstrip() method can be used to strip whitespace FROM THE RIGHT.
favorite_language2 = "Python     "
print(favorite_language.rstrip())

#2.3.4.3
# The .lstrip() method can be used to strip whitespace FROM THE LEFT.
favorite_language3 = "     Python"
print(favorite_language2.lstrip())