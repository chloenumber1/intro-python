# 3.2 Changing, Adding, and Removing Elements

# 3.2.1 Modifying Elements in a List

# 3.2.1.1: Changing an element in a list:
print("Example of changing an item in a list using its position:")
print("Initial contents of the list:")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
print("After changing index 0 to \"ducati\":")
motorcycles[0] = 'ducati'
print(motorcycles)

# 3.2.2 Adding elements to a list:

# 3.2.2.1: Appending elements to the END of a list:
# This is done with the .append() method
print("This is the original motorcycle list:")
motorcycles = ['honda', 'yamaha', 'suzuki']
print("This is the motorcycle list after I used the append method with \"ducati\":")
motorcycles.append("ducati")
print(motorcycles)

#3.2.2.2: Populating the whole list using .append()


