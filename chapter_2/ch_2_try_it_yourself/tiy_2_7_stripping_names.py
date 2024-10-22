# 2-7. Stripping Names: Use a variable to represent a person’s name, 
# and include some whitespace characters at the beginning and end 
# of the name. Make sure you use each character combination, 
# "\t" and "\n", at least once. 
# Print the name once, so the whitespace around the name is displayed. 
# Then print the name using each of the three stripping functions, 
# lstrip(), rstrip(), and strip().

# Print the name once:
whitespace_name = "\n\n\tBug-a-boo\t\n"
print("Printing the name:")
print(whitespace_name)

# Printing with lstrip(), rstrip(), and strip()
print("Printing with lstrip():")
print(whitespace_name.lstrip())
print("Printing with rstrip():")
print(whitespace_name.rstrip())
print("Printing with strip():")
print(whitespace_name.strip())