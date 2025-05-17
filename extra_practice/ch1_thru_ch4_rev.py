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

# Ch.3 was an intro to lists.
# It covered:
# 3.1 What is a list
# 3.2 Changing, adding, and removing elements
# 3.3 Organizing a list

# 3-1. Names: Store the names of a few of your friends in a list called 
# names. Print each person’s name by accessing each element in the list, 
# one at a time.

print("3-1 Names List Question:\n")
names_list3_1 = ["friend1", "friend2", "friend3", "friend4", "friend5"]
print(names_list3_1[0])
print(names_list3_1[1])
print(names_list3_1[2])
print(names_list3_1[3])
print(names_list3_1[4])
print("----------\n")

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead 
# of just printing each person’s name, print a message to them. The text 
# of each message should be the same, but each message should be personalized 
# with the person’s name.
print("3-2 Greetings Question:\n")
print(f"Hi there, {names_list3_1[0].title()}")
print(f"Hi there, {names_list3_1[1].title()}")
print(f"Hi there, {names_list3_1[2].title()}")
print(f"Hi there, {names_list3_1[3].title()}")
print(f"Hi there, {names_list3_1[4].title()}")
print("----------\n")

# 3-3. Your Own List: Think of your favorite mode of transportation, such 
# as a motorcycle or a car, and make a list that stores several examples. 
# Use your list to print a series of statements about these items, such 
# as “I would like to own a Honda motorcycle.”

print("3-3 Your Own List Question:\n")
transport_list3_3 = ["walking", "car", "plane", "cruise ship", "ferry"]
print(f"Sometimes, I don't want to drive, I'd rather be {transport_list3_3[0]}.")
print(f"I usually have to drive a {transport_list3_3[1]} to get anywhere.")
print(f"I typically only take a {transport_list3_3[2]} for vacation, which isn't often.")
print(f"This year, I got to spend 4 days on a {transport_list3_3[3]}.")
print(f"I've only taken a {transport_list3_3[4]} once, but I liked it.")
print("----------\n")

# 3-4. Guest List: If you could invite anyone, living or deceased, 
# to dinner, who would you invite? Make a list that includes at least three
# people you’d like to invite to dinner. Then use your list to print a 
# message to each person, inviting them to dinner.

print("3-4 Guest List Question:\n")
print("----------\n")

# 3-5. Changing Guest List: You just heard that one of your guests can’t 
# make the dinner, so you need to send out a new set of invitations. You’ll
# have to think of someone else to invite.
# 3-5.1 Start with your program from Exercise 3-4. Add a print() call at 
# the end of your program stating the name of the guest who can’t make it.
# 3-5.2 Modify your list, replacing the name of the guest who can’t make 
# it with the name of the new person you are inviting.
# 3-5.3 Print a second set of invitation messages, one for each person 
# who is still in your list.

print("3-5.1 Changing Guest List Question:\n")
print("----------\n")

print("3-5.2 Changing Guest List Question:\n")
print("----------\n")

print("3-5.3 Names Changing Guest Question:\n")
print("----------\n")

# 3-6. More Guests: You just found a bigger dinner table, so now more 
# space is available. Think of three more guests to invite to dinner.
# 3-6.1 Start with your program from Exercise 3-4 or Exercise 3-5. 
# Add a print() call to the end of your program informing people that you 
# found a bigger dinner table.
# 3-6.2 Use insert() to add one new guest to the beginning of your list.
# 3-6.3 Use insert() to add one new guest to the middle of your list.
# 3-6.4 Use append() to add one new guest to the end of your list.
# 3-6.5 Print a new set of invitation messages, one for each person in your list.

print("3-6.1 More Guests Question:\n")
print("----------\n")

print("3-6.2 More Guests Question:\n")
print("----------\n")

print("3-6.3 More Guests Question:\n")
print("----------\n")

print("3-6.4 More Guests Question:\n")
print("----------\n")

print("3-6.5 More Guests Question:\n")
print("----------\n")

# 3-7. Shrinking Guest List: You just found out that your new dinner table
# won’t arrive in time for the dinner, and you have space for only two guests.
# 3-7.1 Start with your program from Exercise 3-6. Add a new line that prints
# a message saying that you can invite only two people for dinner.
# 3-7.2 Use pop() to remove guests from your list one at a time until only 
# two names remain in your list. Each time you pop a name from your list, 
# print a message to that person letting them know you’re sorry you can’t 
# invite them to dinner.
# 3-7.3 Print a message to each of the two people still on your list, letting 
# them know they’re still invited.
# 3-7.4 Use del to remove the last two names from your list, so you have an empty 
# list. Print your list to make sure you actually have an empty list at the end 
# of your program.

print("3-7.1 Shrinking Guest List Question:\n")
print("----------\n")

print("3-7.2 Shrinking Guest List Question:\n")
print("----------\n")

print("3-7.3 Shrinking Guest List Question:\n")
print("----------\n")

print("3-7.4 Shrinking Guest List Question:\n")
print("----------\n")

# 3-8. Seeing the World: Think of at least five places in the world you’d like to 
# visit.
# 3-8.1 Store the locations in a list. Make sure the list is not in alphabetical 
# order.
# 3-8.2 Print your list in its original order. Don’t worry about printing the 
# list neatly, just print it as a raw Python list.
# 3-8.3 Use sorted() to print your list in alphabetical order without modifying the 
# actual list.
# 3-8.4 Show that your list is still in its original order by printing it.
# 3-8.5 Use sorted() to print your list in reverse alphabetical order without 
# changing the order of the original list.
# 3-8.6 Show that your list is still in its original order by printing it again.
# 3-8.7 Use reverse() to change the order of your list. Print the list to show 
# that its order has changed.
# 3-8.8 Use reverse() to change the order of your list again. Print the list to 
# show it’s back to its original order.
# 3-8.9 Use sort() to change your list so it’s stored in alphabetical order. 
# Print the list to show that its order has been changed.
# 3-8.10 Use sort() to change your list so it’s stored in reverse 
# alphabetical order. Print the list to show that its order has changed.

print("3-8.1 Seeing The World Question:\n")
print("----------\n")

print("3-8.2 Seeing The World Question:\n")
print("----------\n")

print("3-8.3 Seeing The World Question:\n")
print("----------\n")

print("3-8.4 Seeing The World Question:\n")
print("----------\n")

print("3-8.5 Seeing The World Question:\n")
print("----------\n")

print("3-8.6 Seeing The World Question:\n")
print("----------\n")

print("3-8.7 Seeing The World Question:\n")
print("----------\n")

print("3-8.8 Seeing The World Question:\n")
print("----------\n")

print("3-8.9 Seeing The World Question:\n")
print("----------\n")

print("3-8.10 Seeing The World Question:\n")
print("----------\n")

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 
# through 3-7 (page 42), use len() to print a message indicating the number 
# of people you are inviting to dinner.

print("3-9 Dinner Guests Question:\n")
print("----------\n")

# 3-10. Every Function: Think of something you could store in a list. For example, 
# you could make a list of mountains, rivers, countries, cities, languages, or 
# anything else you’d like. Write a program that creates a list containing these 
# items and then uses each function introduced in this chapter at least once.

print("3-10 Every Function Question:\n")
print("----------\n")

# 3-11. Intentional Error: If you haven’t received an index error in one of your 
# programs yet, try to make one happen. Change an index in one of your 
# programs to produce an index error. Make sure you correct the error before 
# closing the program.

print("3-11 Intentional Error Question:\n")
print("----------\n")