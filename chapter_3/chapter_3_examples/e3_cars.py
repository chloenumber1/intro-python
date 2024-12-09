# Examples for 3.3 Organizing a List

# 3.3.1.1 The sort() method (default)
# Output: ['audi', 'bmw', 'subaru', 'toyota'] 
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# 3.3.1.1 The sort() method (default, but with numbers)
# Output: [1, 2, 27, 87]
nums = [87, 2, 1, 27]
nums.sort()
print(nums)

# 3.3.2.1
# Output: ['toyota', 'subaru', 'bmw', 'audi']
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# Output: [87, 27, 2, 1]
nums = [87, 2, 1, 27]
nums.sort(reverse=True)
print(nums)

# 3.3.2 Sorting with the sorted() Function
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
# 3.3.2.2 Assignment with the sorted() Function (don't do it)
print("What happens if you ASSIGN the sorted() list instead of just printing it?")
print("This corresponds with the code cars = sorted(cars):")
cars = sorted(cars)
print(cars)
# Now I reassign it to its original form:
cars = ['bmw', 'audi', 'toyota', 'subaru']
