from binary_search_tree import BSTNode
import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

# f = open('names_2.txt', 'r')
# names_2 = f.read().split("\n")
# f.close()

bst = None
with open('names_2.txt', 'r') as fp:
    line = fp.readline()
    while line:
        if not bst:
            bst = BSTNode(line.strip())
        else:
            bst.insert(line.strip())
        line = fp.readline()


duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

# **** OLD RUNTIME COMPLEXITY ****
# This block of code could be said to be O(n*m) where n represents 
# the names in names_1, and m represents the names in names_2.
# Since both of the files have the same amount of names, you could
# also say that it is roughly O(n^2).
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)       
            
# **** IMPROVED CODE RUNTIME COMPLEXITY ****
# O(n log n)
for name in names_1:
    if bst.contains(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
