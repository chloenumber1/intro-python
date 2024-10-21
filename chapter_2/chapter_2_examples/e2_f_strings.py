# Formatted string AKA F-string example from p.21

print("This example shows that you can use a F-String to use variables in a string")
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

print("This example shows that you can 1. save a F-String to a variable and 2. use a method on one of your variables with a F-String")
# Remember: full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

print("This example shows that you can save the prior example's F-string to a variable and then print that variable")
# In the last name we printed the statement. Now we're saving it to 
# a variable named message
message = f"Hello, {full_name.title()}!"
print(message)