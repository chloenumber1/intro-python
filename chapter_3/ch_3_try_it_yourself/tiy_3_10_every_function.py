# 3-10. Every Function: Think of something you could store in a list. 
# For example, you could make a list of mountains, rivers, countries, 
# cities, languages, or anything else you’d like. Write a program that 
# creates a list containing these items and then uses
# each function introduced in this chapter at least once.

# My list of Great Lakes

gr8_lakes = ["huron", "erie", "ontario", "michigan", "superior"]

# sorted()
print(f"This is the list in alphebetical order: {sorted(gr8_lakes)}")

# sorted with reverse parameter
print(f"This is the list in reverse alphebetical order: {sorted(gr8_lakes, reverse=True)}")



# len()
print(f"This is how long the list is: {len(gr8_lakes)}")