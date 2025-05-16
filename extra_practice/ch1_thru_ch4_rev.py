# This is a supplemental review of everything I've covered in 
# Ch.1 through Ch.4.

# Ch.1 was an intro, so I won't be doing review questions 
# for that chapter.

# Ch.2 covered variables, Strings, numbers, and comments.

# 2-1. Simple Message: Assign a message to a variable, and then print that 
# message.

print("2-1 Simple Message Question:\n")
message2_1 = "This is the message for question 2-1."
print(message2_1)
print("----------\n")

# 2-2. Simple Messages: Assign a message to a variable, and print that 
# message. Then change the value of the variable to a new message, 
# and print the new message.

print("2-2 Simple Messages Question:\n")
message2_2 = "This is the original message for question 2-2."
print(message2_2)
# Now reassign the variable, it will no longer contains the original message.
message2_2 = "This is the new message for question 2-2."
print(message2_2)
print("----------\n")

# 2-3. Personal Message: Use a variable to represent a person’s name, 
# and print a message to that person. Your message should be simple, 
# such as, “Hello Eric, would you like to learn some Python today?”

print("2-3 Personal Messages Question:\n")
name2_3 = "Chloe"
print(f"My name is {name2_3}")
print("----------\n")

# 2-4. Name Cases: Use a variable to represent a person’s name, and then 
# print that person’s name in lowercase, uppercase, and title case.

print("2-4 Name Cases Question:\n")
name2_4 = "Eolhc"
print(f"My name is {name2_4.title()}")
print(f"My name is {name2_4.lower()}")
print(f"My name is {name2_4.upper()}")
print("----------\n")

# 2-5. Famous Quote: Find a quote from a famous person you admire. Print 
# the quote and the name of its author. Your output should look something 
# like the following, including the quotation marks:
# Albert Einstein once said, 
#     “A person who never made a 
#     mistake never tried anything new.”

print("2-5 Famous Quote Question:\n")
name2_5 = "Chloe's Mom"
print(f"{name2_5} once said,")
print("\t\"Stop")
print("\tbeing")
print("\tDUMB!!!!\"")
print("...And to that I said \"no\"")
print("----------\n")

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the 
# famous person’s name using a variable called famous_person. 
# Then compose your  message and represent it with a new variable called 
# message. Print your message.

print("2-6 Famous Quote Question:\n")
name2_6 = "Chloe's Mom"
message = f"{name2_6} once said,\n\t\"Stop\tbeing\tDUMB!!!!\"\n...And to that I said \"no\""
print(message)
print("----------\n")

# 2-7. Stripping Names: Use a variable to represent a person’s name, and 
# include some whitespace characters at the beginning and end of the name. 
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed. 
# Then print the name using each of the three stripping functions, lstrip(), 
# rstrip(), and strip()

print("2-7 Stripping Names Question:\n")
name2_7 = "\t\n\tChloe\n\t\n"
print("Original name:")
print(name2_7)
print("Name with lstrip():")
print(name2_7.lstrip())
print("Name with rstrip():")
print(name2_7.rstrip())
print("Name with strip():")
print(name2_7.strip())
print("----------\n")

# 2-8. Number Eight: Write addition, subtraction, multiplication, and 
# division operations that each result in the number 8. Be sure to 
# enclose your operations in print() calls to see the results. You 
# should create four lines that look like this: print(5+3)
# Your output should simply be four lines with the number 8 appearing
# once on each line.

print("2-8 Number Eight Question:\n")
print(4+4)
print(12-4)
print(2*4)
print(16/2)
print("----------\n")

# 2-9. Favorite Number: Use a variable to represent your favorite number. 
# Then, using that variable, create a message that reveals your favorite 
# number. Print that message.

print("2-9 Favorite Number Question:\n")
fav_num = 28.0
print(f"This is my favorite number: {fav_num}")
print("----------\n")

# 2-10 was about adding comments, which are throughout the file.