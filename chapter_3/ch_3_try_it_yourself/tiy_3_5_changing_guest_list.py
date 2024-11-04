# 3-5. Changing Guest List: You just heard that one of your guests 
# can’t make the dinner, so you need to send out a new set of invitations. 
# You’ll have to think of someone else to invite.
# 1. Start with your program from Exercise 3-4. Add a print() call at the 
# end of your program stating the name of the guest who can’t make it.
# 2. Modify your list, replacing the name of the guest who can’t make it 
# with the name of the new person you are inviting.
# 3. Print a second set of invitation messages, one for each person who is 
# still in your list

# 1. Start with your program from Exercise 3-4. Add a print() call at the 
# end of your program stating the name of the guest who can’t make it.

# Making a list of invites

invite = ["Mom", "William Shakespeare", "Jesus", "Moo Deng", "Pablo Picasso"]

# Printing invites to each one using a formatted string with their element index

print(f"Hi {invite[0]}, I would love to have you at my dinner party!")
print(f"Hi {invite[1]}, I would love to have you at my dinner party!")
print(f"Hi {invite[2]}, I would love to have you at my dinner party!")
print(f"Hi {invite[3]}, I would love to have you at my dinner party!")
print(f"Hi {invite[4]}, I would love to have you at my dinner party!")
print(f"Dang! {invite[3]} can't make it.")
print(f"Old invitation list: {invite}")
print()

# 2. Modify your list, replacing the name of the guest who can’t make it 
# with the name of the new person you are inviting.
invite[3] = "Grigori Rasputin"
print()

# 3. Print a second set of invitation messages, one for each person who is 
# still in your list
print("These are the new invitation messages:")
print(f"Hi {invite[0]}, I would love to have you at my dinner party!")
print(f"Hi {invite[1]}, I would love to have you at my dinner party!")
print(f"Hi {invite[2]}, I would love to have you at my dinner party!")
print(f"Hi {invite[3]}, I would love to have you at my dinner party!")
print(f"Hi {invite[4]}, I would love to have you at my dinner party!")
print(f"New invitation list: {invite}")