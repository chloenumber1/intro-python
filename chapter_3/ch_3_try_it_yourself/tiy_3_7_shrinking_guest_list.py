# 3-7. Shrinking Guest List: You just found out that your new dinner table 
# won’t arrive in time for the dinner, and you have space for only two guests.
# 1. Start with your program from Exercise 3-6. Add a new line that 
# prints a message saying that you can invite only two people for dinner.
# 2. Use pop() to remove guests from your list one at a time until only two 
# names remain in your list. Each time you pop a name from your list, print 
# a message to that person letting them know you’re sorry you can’t invite 
# them to dinner.
# 3. Print a message to each of the two people still on your list, 
# letting them know they’re still invited.
# 4. Use del to remove the last two names from your list, so you have an 
# empty list. Print your list to make sure you actually have an empty list at 
# the end of your program

invite = ["Mom", "William Shakespeare", "Jesus", "Moo Deng", "Pablo Picasso"]

print(f"Hi {invite[0]}, I would love to have you at my dinner party!")
print(f"Hi {invite[1]}, I would love to have you at my dinner party!")
print(f"Hi {invite[2]}, I would love to have you at my dinner party!")
print(f"Hi {invite[3]}, I would love to have you at my dinner party!")
print(f"Hi {invite[4]}, I would love to have you at my dinner party!")
print(f"Dang! {invite[3]} can't make it.")
print(f"Old invitation list: {invite}")
print()

invite[3] = "Grigori Rasputin"
print()

print("These are the new invitation messages:")
print(f"Hi {invite[0]}, I would love to have you at my dinner party!")
print(f"Hi {invite[1]}, I would love to have you at my dinner party!")
print(f"Hi {invite[2]}, I would love to have you at my dinner party!")
print(f"Hi {invite[3]}, I would love to have you at my dinner party!")
print(f"Hi {invite[4]}, I would love to have you at my dinner party!")
print(f"New invitation list: {invite}")
print("Hey everyone, I found a bigger table for us.")
print()

# Use insert() to add one new guest to the beginning of your list.
invite.insert(0, "Cathie Wood")

# Use insert() to add one new guest to the middle of your list.
invite.insert(3, "Mary Shelley")

# Use append() to add one new guest to the end of your list.
invite.append("Grandma")

# Print a new set of invitation messages, one for each person in your list.
print("These are the newer invitation messages with people added:")
print(f"Hi {invite[0]}, I would love to have you at my dinner party!")
print(f"Hi {invite[1]}, I would love to have you at my dinner party!")
print(f"Hi {invite[2]}, I would love to have you at my dinner party!")
print(f"Hi {invite[3]}, I would love to have you at my dinner party!")
print(f"Hi {invite[4]}, I would love to have you at my dinner party!")
print(f"Hi {invite[5]}, I would love to have you at my dinner party!")
print(f"Hi {invite[6]}, I would love to have you at my dinner party!")
print(f"Hi {invite[7]}, I would love to have you at my dinner party!")
print(f"New invitation list: {invite}")

# --- Beginning of Try-It-Yourself 3-7 ---
# 1. Start with your program from Exercise 3-6. Add a new line that 
# prints a message saying that you can invite only two people for dinner.
print("\n Unfortunately, I can only invite two people for dinner since my table hasn't arrived.")

# I don't want to do it index-by-index, I want to use the length.
guest_list_length = len(invite)

# 2. Use pop() to remove guests from your list one at a time until only two 
# names remain in your list. Each time you pop a name from your list, print 
# a message to that person letting them know you’re sorry you can’t invite 
# them to dinner.

# This is task 2, part 1
# I have to pop the last 6 guests, but since I have to write messages,
# I will have to save them to a variable for later use.
guest_list_8 = invite.pop(guest_list_length-1)
guest_list_7 = invite.pop(guest_list_length-2)
guest_list_6 = invite.pop(guest_list_length-3)
guest_list_5 = invite.pop(guest_list_length-4)
guest_list_4 = invite.pop(guest_list_length-5)
guest_list_3 = invite.pop(guest_list_length-6)

# This is task 2, part 2
# Printing my apology messages for all of the 6 guests I popped
print(f"I'm so sorry, {guest_list_8}, I can't invite you!")
print(f"I'm so sorry, {guest_list_7}, I can't invite you!")
print(f"I'm so sorry, {guest_list_6}, I can't invite you!")
print(f"I'm so sorry, {guest_list_5}, I can't invite you!")
print(f"I'm so sorry, {guest_list_4}, I can't invite you!")
print(f"I'm so sorry, {guest_list_3}, I can't invite you!")

# 3. Print a message to each of the two people still on your list, 
# letting them know they’re still invited.
print(f"Hi, {invite[0]} you're still invited!")
print(f"Hi, {invite[1]} you're still invited!")

# 4. Use del to remove the last two names from your list, so you have an 
# empty list. Print your list to make sure you actually have an empty list at 
# the end of your program
del invite[1]
del invite[0]
print(invite)