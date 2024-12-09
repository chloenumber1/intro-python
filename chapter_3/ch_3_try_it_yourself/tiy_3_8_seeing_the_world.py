# 3-8. Seeing the World: Think of at least five places in the world you’d 
# like to visit.
# 1. Store the locations in a list. Make sure the list is not in 
# alphabetical order.
# 2. Print your list in its original order. Don’t worry about printing the 
# list neatly, just print it as a raw Python list.
# 3. Use sorted() to print your list in alphabetical order without modifying
# the actual list.
# 4. Show that your list is still in its original order by printing it.
# 5. Use sorted() to print your list in reverse alphabetical order without 
# changing the order of the original list.
# 6. Show that your list is still in its original order by printing it again.
# 7. Use reverse() to change the order of your list. Print the list to show 
# that its order has changed.
# 8. Use reverse() to change the order of your list again. Print the list to
# show it’s back to its original order.
# 9. Use sort() to change your list so it’s stored in alphabetical order. 
# Print the list to show that its order has been changed.
# 10. Use sort() to change your list so it’s stored in reverse alphabetical 
# order. Print the list to show that its order has changed.

# 1 and 2: Thinking of where I want to go, making the list, and printing the list
travel_list = ["hawaii","alaska","argentina","liechtenstein", "south korea"]
print(travel_list)

# 3. Use sorted() to print your list in alphabetical order without modifying
# the actual list.
print(f"Applying the sorted() Function: {sorted(travel_list)}")

# 4. Show that your list is still in its original order by printing it.
print(f"Proving that the actual list is the same: {travel_list}")

# 5. Use sorted() to print your list in reverse alphabetical order without 
# changing the order of the original list.
print(f"Reversed list using sorted(travel_list,reverse=True): {sorted(travel_list,reverse=True)}")

# 6. Show that your list is still in its original order by printing it again.
print(f"The list is still the same: {travel_list}")

# 7. Use reverse() to change the order of your list. Print the list to show 
# that its order has changed.
travel_list.reverse()
print(f"The travel list once the reverse() Method is used: {travel_list}")

# 8. Use reverse() to change the order of your list again. Print the list to
# show it’s back to its original order.
travel_list.reverse()
print(f"The original travel list once the reverse() Method is used again: {travel_list}")

# 9. Use sort() to change your list so it’s stored in alphabetical order. 
# Print the list to show that its order has been changed.
travel_list.sort()
print(f"Sorted alphebetically with sort(): {travel_list}")

# 10. Use sort() to change your list so it’s stored in reverse alphabetical 
# order. Print the list to show that its order has changed.
travel_list.sort(reverse=True)
print(f"Sorted reverse alphebetically with sort(reverse=True): {travel_list}")