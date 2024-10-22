# A common syntax error that can occur is if you write a string 
# such as 'This string 'in single quotes' here.' 
# What will happen is that Python can't identify where the string 
# starts and ends. 

# 2.3.5.2
# These examples generate an error because what will happen is 
# that Python can't identify where the string starts and ends.

# Error code with all single quotes:
print('This string 'has a single quote' and creates an error')

# Error code with all double quotes:
print("This string "has a double quote" and creates an error")

# 2.3.5.3
# These examples won't generate an error because there's no 
# ambiguity as to where the quote starts and stops. 

# Example of double quotes on the outside to print single quotes in the string:
print("This string has a 'single quote' in it but it does not generate an error.")

# Example of single quotes on the outside to print double quotes in the string:
print('This string has a "double quote" in it but it does not generate an error.')