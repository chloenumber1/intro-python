# 4.1.1.2 
# Introducing the for loop syntax
print("4.1.1.2 Introducing for loop syntax")
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician)

# 4.1.2.1
# Formatted string with for loop
print("\n4.1.2.1 Formatted string with a for loop")
magicians2 = ['alice', 'david', 'carolina'] 
for magician in magicians2: 
    print(f"{magician.title()}, that was a great trick!") 

# 4.1.2.2 
# Two formatted strings with a for loop
("\n4.1.2.2 Two formatted strings in a for loop")
magicians3 = ['alice', 'david', 'carolina'] 
for magician in magicians3:
    print(f"{magician.title()}, that was a great trick!") 
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# 4.1.3.1
# Doing something outside of a loop
print("\n4.1.3.1 Doing something outside of a loop")
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
 print(f"{magician.title()}, that was a great trick!")
 print(f"I can't wait to see your next trick, {magician.title()}.\n")
 
print("Thank you, everyone. That was a great magic show!")

# 4.2.1.1
# Forgetting to indent

print("\n4.2.1.1 This code generates an error because the for loop body isn't indented.")
# magicians = ['alice', 'david', 'carolina'] 
# for magician in magicians: 
# print(magician)

# 4.2.2.1
# Forgetting to indent ADDITIONAL lines

print("\n4.2.2.1 This code produces unexpected output because one of the print statements in the loop body isn't indented.")
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")

# 4.2.3.1
# Indenting unnecessarily

print("\n4.2.3.1 Indenting unnecessarily will generate an error")
# message = "Hello Python world!"
#    print(message)

# 4.2.4.1
# Indenting unnecessarily AFTER the loop

print("\n4.2.4.1 Indenting unnecessarily AFTER the loop will cause the indented line to be included in the loop")
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n") 
    print("Thank you everyone, that was a great magic show!")

# 4.2.5.1
# Forgetting the colon
print("4.2.5.1 Forgetting the colon will cause a syntax error")
# magicians = ['alice', 'david', 'carolina'] 
# for magician in magicians
#     print(magician)