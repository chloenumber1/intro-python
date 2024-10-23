# 3.1.1 Defining a List
bicycles = ["trek","canondale","redline","specialized"]
print("This is printing the whole list:")
print(bicycles)

# 3.1.2 Accessing Elements in a List 

# 3.1.2.1 Accessing Elements Using an Index
# This code is saying "access the element in the first position 
# in the bicycles list"
print("Accessing an element using its index:")
print(bicycles[0])

# 3.1.2.2 Accessing Elements Using an Index and Adding a Method
# This code is saying "access the element in the first position 
# in the bicycles list and put it in all capital letters"
print("Printing the first element in the list and using the .upper() method:")
print(bicycles[0].upper())

# 3.1.3 Index Positions Start at 0, Not 1

# 3.1.3.1 Zero-indexing
# If you print the element at index 1, you get the element in the second position.
print("This is printing the element at index 1:")
print(bicycles[1])
# If you print the element at index 0, you get the first element
print("This is printing the element at index 0:")
print(bicycles[0])

# 3.1.3.2 Index -1
print("Printing element -1:")
print(bicycles[-1])

# 3.1.4 Using Individual Values From a List
print(f"This is a formatted string using an element from the list. I'll call the last element: {bicycles[-1]}")

# 