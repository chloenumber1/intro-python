# A common syntax error that can occur is if you write a string 
# such as 'This string 'in single quotes' here.' 
# What will happen is that Python can't identify where the string 
# starts and ends. 

# 2.3.5.2
# This example generates an error because what will happen is 
# that Python can't identify where the string starts and ends.

print('This string 'has a single quote' and creates an error')

# 2.3.5.3
# This example won't generate an error because there's no 
# ambiguity as to where the quote starts and stops. 

print("This string has a 'single quote' in it but it doesn't generate an error.")