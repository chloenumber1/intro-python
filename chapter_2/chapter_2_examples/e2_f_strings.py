# 2.3.2.2 and 2.3.2.3
print("This example shows that you can use a F-String to use variables in a string")
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

# 2.3.2.4
print("This example shows that you can 1. save a F-String to a variable and 2. use a method on one of your variables with a F-String")
# Remember: full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

# 2.3.2.5
print("This example shows that you can save the prior example's F-string to a variable and then print that variable")
# In the last name we printed the statement. Now we're saving it to 
# a variable named message
message = f"Hello, {full_name.title()}!"
print(message)