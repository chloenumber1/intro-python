# 4.1.1.2 
# Introducing the for loop syntax
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician)

# 4.1.2.1
# Formatted string with for loop
magicians2 = ['alice', 'david', 'carolina'] 
for magician in magicians2: 
    print(f"{magician.title()}, that was a great trick!") 

# 4.1.2.2 
# Two formatted strings with a for loop
magicians3 = ['alice', 'david', 'carolina'] 
for magician in magicians3:
    print(f"{magician.title()}, that was a great trick!") 
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# 4.1.3.1
# Doing something outside of a loop
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
 print(f"{magician.title()}, that was a great trick!")
 print(f"I can't wait to see your next trick, {magician.title()}.\n")
 
u print("Thank you, everyone. That was a great magic show!")
