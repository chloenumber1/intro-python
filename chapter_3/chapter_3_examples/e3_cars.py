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