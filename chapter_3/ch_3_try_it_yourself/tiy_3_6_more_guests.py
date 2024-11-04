# 3-6. More Guests: You just found a bigger dinner table, so now more 
# space is available. Think of three more guests to invite to dinner.
# 1. Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# call to the end of your program informing people that you found a bigger 
# dinner table.
# 2. Use insert() to add one new guest to the beginning of your list.
# 3. Use insert() to add one new guest to the middle of your list.
# 4. Use append() to add one new guest to the end of your list.
# 5. Print a new set of invitation messages, one for each person in your list.

# 1. Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# call to the end of your program informing people that you found a bigger 
# dinner table.

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

# 2. Use insert() to add one new guest to the beginning of your list.
invite.insert(0, "Cathie Wood")

# 3. Use insert() to add one new guest to the middle of your list.
invite.insert(3, "Mary Shelley")

# 4. Use append() to add one new guest to the end of your list.
invite.append("Grandma")

# 5. Print a new set of invitation messages, one for each person in your list.
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