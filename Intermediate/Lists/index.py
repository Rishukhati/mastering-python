# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]
# print(numbers)
# print(len(numbers))

# Creating a list of strings
fruits = ["apple", "orange", "banana", "grape"]
# print(fruits)
# print(len(fruits))

# Creating a mixed-type list
mixed_list = [1, "hello", 3.14, True]
print(mixed_list)
print(len(mixed_list))

# ----------------------------------

# Accessing Item
# my_list = [1, 2, 3, 4, 5]

# print(my_list[0])
# print(my_list[2])

# Negative indexing can be used to access items from the end of the list
# print(my_list[-1])
# print(my_list[-2])
# ----------------------------------

# ----------------------------------
# Using Slices
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

subset = my_list[2:6]
print(subset)  # [2, 3, 4, 5]

# Omitting start and stop indices
subset = my_list[:5]
print(subset)  # [0, 1, 2, 3, 4]

subset = my_list[5:]
print(subset)  # [5, 6, 7, 8, 9]

# Using negative indices
subset = my_list[-3:]  # Gets the last 3 elements
print(subset)  # [7, 8, 9]

# Using step
subset = my_list[1:9:2]
print(subset)  # [1, 3, 5, 7]




# ----------------------------
my_list = [1, 2, 3, 4, 5]

my_list[2] = 10     # for deleting anything from list we use del reserve key word del my_list[index]  or we can use remove() like my_list.remove(here we enter number)
print(my_list)


# ----------------------------
# Create a 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Update the element at the second row and third column (index 1, 2)
matrix[1][2] = 10

# Print the updated matrix
print("\nUpdated Matrix:")
for row in matrix:
    print(row)

# LIST BUILD-IN METHODS

# append
my_list = [1, 2, 3]
my_list.append(4)

# extend
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])

# insert
my_list = [1, 2, 3]
my_list.insert(1, 4)

# remove
my_list = [1, 2, 3, 2]
my_list.remove(2)

# pop
my_list = [1, 2, 3]
popped_element = my_list.pop(1)

# count
my_list = [1, 2, 3, 2]
count_of_2 = my_list.count(2)

# sort
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
my_list.sort()

# reverse
my_list = [1, 2, 3]
my_list.reverse()

# copy
original_list = [1, 2, 3]
copied_list = original_list.copy()







