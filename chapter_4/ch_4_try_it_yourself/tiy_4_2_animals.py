# 4-2.1. Animals: Think of at least three different animals that 
# have a common characteristic. Store the names of these animals in
# a list, and then use a for loop to print out the name of each animal.
# 4-2.2 Modify your program to print a statement about each animal, such as 
# A dog would make a great pet.
# 4-2.3 Add a line at the end of your program stating what these animals have 
# in common. You could print a sentence such as Any of these animals would 
# make a great pet!

print("4-2.1 Listing the Animals")
animals_4_2_1 = ["shih tzu", "bunny", "red panda", "himalayan cat", "chinchilla"]
for animal in animals_4_2_1:
    print(animal)
print("-----End of 4-2.1-----\n")   

print("4-2.2 Printing a Statement in the Animal loop")
animals_4_2_2 = ["shih tzu", "bunny", "red panda", "mini horse", "chinchilla"]
for animal in animals_4_2_2:
    print(f"{animal} is so cute and fun.")
print("-----End of 4-2.2-----\n")

print("4-2.3 Printing Outside of the Animal loop")
animals_4_2_3 = ["shih tzu", "bunny", "red panda", "otter", "chinchilla"]
for animal in animals_4_2_3:
    print(f"{animal} is so cute and fun, I want to pet it.")
print("All of these animals are super cute and fuzzy")
print("-----End of 4-2.2-----\n")