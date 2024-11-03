# 3.2 Changing, Adding, and Removing Elements

# 3.2.1 Modifying Elements in a List

# 3.2.1.1: Changing an element in a list:
print("Example of changing an item in a list using its position:")
print("Initial contents of the list:")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
print("After changing index 0 to \"ducati\":")
motorcycles[0] = "ducati"
print(motorcycles)
print()

# 3.2.2 Adding elements to a list:

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

