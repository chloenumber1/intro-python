# 4-1.1 Pizzas: Think of at least three kinds of your favorite pizza. 
# Store these pizza names in a list, and then use a for loop to print 
# the name of each pizza.
# 4-1.2	Modify your for loop to print a sentence using the name of the 
# pizza instead of printing just the name of the pizza. For each pizza you 
# should have one line of output containing a simple statement like I like 
# pepperoni pizza.
# 4-1.3 Add a line at the end of your program, outside the for loop, 
# that states how much you like pizza. The output should consist of three 
# or more lines about the kinds of pizza you like and then an additional sentence, 
# such as I really love pizza!

print("4-1.1 Printing the pizza list")
pizzas_4_1_1 = ["gyro pizza", "pan pizza", "Sicilian pizza", "pizza bagel", "NY pizza"]
for pizza in pizzas_4_1_1:
    print(pizza)
print("-----End of 4-1.1-----\n")

print("4-1.2 Printing a statement in the pizza loop")
pizzas_4_1_2 = ["alfredo pizza", "pan pizza", "stuffed crust pizza", "pizza bagel", "NY pizza"]
for pizza in pizzas_4_1_2:
    print(f"One of my favorite kinds of pizza is {pizza.upper()}!!!")
print("-----End of 4-1.2-----\n")

print("4-1.3 Printing outside of the pizza loop")
pizzas_4_1_3 = ["alfredo pizza", "pan pizza", "stuffed crust pizza", "pizza bagel", "buffalo chicken pizza"]
for pizza in pizzas_4_1_3:
    print(f"One of my favorite kinds of pizza is {pizza.upper()}!!!")
print("Although I like those pizzas...")
print("I think my favorite pizza is actually Costco pizza.")
print("-----End of 4-1.3-----\n")