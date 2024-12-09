# 3-11. Intentional Error: If you haven’t received an index error in 
# one of your programs yet, try to make one happen. Change an index 
# in one of your programs to produce an index error. Make sure you correct 
# the error before closing the program.

# I generated an error similar to this, so I'll show it.
sample_list = [0, "hi", 2.7, 87, "boo"]

# del sample_list[-1]
# del sample_list[-1]
# del sample_list[-1]
# del sample_list[0]
# del sample_list[1]

# The problem is that I deleted the index 0, 
# which left just one item at index 0 but instead of
# deleting index 0 again, I tried to delete index 1, which didnt exist.

# The fix:
del sample_list[-1]
del sample_list[-1]
del sample_list[-1]
del sample_list[-1]
del sample_list[0]
print(sample_list)