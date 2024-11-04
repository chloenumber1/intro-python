# 3.2 Changing, Adding, and Removing Elements

# 3.2.1 Modifying Elements in a List
# Changing an item in a list using its index

# 3.2.1.1: Changing an element in a list:
print("Example of changing an item in a list using its position:")
print("Initial contents of the list:")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
print("After changing index 0 to \"ducati\":")
motorcycles[0] = "ducati"
print(motorcycles)
print()

# 3.2.2 Adding elements to a list
# These examples are using the .append() method

# 3.2.2.1: Appending elements to the END of a list:
# This is done with the .append() method
print("Example using the .append() method:")
print("This is the original motorcycle list:")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
print("This is the motorcycle list after I used the append method with \"ducati\":")
motorcycles.append("ducati")
print(motorcycles)
print()

#3.2.2.2: Populating the whole list using .append()
print("In this example, I am populating a list using the .append() method.")
new_motorcycles = []
print("This is an empty list named new_motorcycles. I'm printing its initial contents (nothing):")
print(new_motorcycles)
print("Now, I am adding items one-by-one using the .append() method:")
new_motorcycles.append("BMW")
print(new_motorcycles)
new_motorcycles.append("Yamaha")
print(new_motorcycles)
new_motorcycles.append("Moto Guzzi")
print(new_motorcycles)
print("This is the full new_motorcycles list:")
print(new_motorcycles)
print()

# 3.2.3 Removing Items from a List
# These examples are the del statement, pop() method, popping any item, and using position in the list.

# 3.2.3.1 The del statement
print("Using the new_motorcycles list, I want to remove \"Moto Guzzi\", which is at index 2:")
print(f"Initial list : {new_motorcycles}")
del new_motorcycles[2]
print(f"List after removing the item at index 2: {new_motorcycles}")
print()

# 3.2.3.2 The pop() method's default behavior
# Important note: whenever you use the pop() method, 
# remember that the element you pop gets removed from the list.

# 3.2.3.2.2 The pop() method's default behavior
print("This is an example of the pop() method.")
new_motorcycles = ["BMW", "Yamaha", "Moto Guzzi"]
print(f"This is the contents of new_motorcycles:{new_motorcycles}")
popped_new_motorcycles = new_motorcycles.pop()
print(f"This is the contents of popped_new_motorcycles: {popped_new_motorcycles}")
print(f"This is the contents of new_motorcycles: {new_motorcycles}")
print()

# 3.2.3.3.3 The pop() method with an index
print("This is the pop() method with an index")
first_motorcycle = new_motorcycles.pop(0)
print(f"This first motorcycle I ever owned was a {first_motorcycle}")
print()

# 3.2.3.4 Removing an item with the del() method

# 3.2.3.4.1 .remove() syntax
print("You can remove items of any type by using .remove().")
mult_types_list = [1, "hi", 3.14, True]
print(f"This is the contents of mult_types_list: {mult_types_list}")
print("Now I'll remove each list element and print it as I go along.")
mult_types_list.remove("hi")
print(f"I removed the element \"hi\": {mult_types_list}")
mult_types_list.remove(1)
print(f"I removed the element 1: {mult_types_list}")
mult_types_list.remove(True)
print(f"I removed the element True: {mult_types_list}")
mult_types_list.remove(3.14)
print(f"I removed the element 3.14: {mult_types_list}")
