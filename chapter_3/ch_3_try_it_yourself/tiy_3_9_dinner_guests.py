# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 
# through 3-7 (page 42), use len() to print a message indicating the number 
# of people you are inviting to dinner.

# Making a list of invites

invite = ["Mom", "William Shakespeare", "Jesus", "Moo Deng", "Pablo Picasso"]

# Storing the number of guests:
num_guests = len(invite)

# Printing invites to each one using a formatted string with their element index

print(f"Hi {invite[0]}, I would love to have you at my dinner party!")
print(f"Hi {invite[1]}, I would love to have you at my dinner party!")
print(f"Hi {invite[2]}, I would love to have you at my dinner party!")
print(f"Hi {invite[3]}, I would love to have you at my dinner party!")
print(f"Hi {invite[4]}, I would love to have you at my dinner party!")
print(f"This means, we will have {num_guests} attendees!")