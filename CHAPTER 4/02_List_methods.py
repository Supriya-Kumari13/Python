# Demonstrating some of the most useful list methods in Python

# 1. append() - Adds an element to the end of the list
my_list = [1, 2, 3]
my_list.append(4)
print("After append:", my_list)  # Output: [1, 2, 3, 4]

# 2. extend() - Extends the list by appending elements from another iterable
my_list.extend([5, 6])
print("After extend:", my_list)  # Output: [1, 2, 3, 4, 5, 6]

# 3. insert() - Inserts an element at a specified position
my_list.insert(2, 99)
print("After insert:", my_list)  # Output: [1, 2, 99, 3, 4, 5, 6]

# 4. remove() - Removes the first occurrence of a specified value
my_list.remove(99)
print("After remove:", my_list)  # Output: [1, 2, 3, 4, 5, 6]

# 5. pop() - Removes and returns the element at a specified position (default is the last element)
last_item = my_list.pop(3)
print("After pop:", my_list)  # Output: [1, 2, 3, 4, 5]
print("Popped item:", last_item)  # Output: 6

# 6. index() - Returns the index of the first occurrence of a specified value
index_of_4 = my_list.index(4)
print("Index of 4:", index_of_4)  # Output: 3

# 7. count() - Returns the number of occurrences of a specified value
count_of_2 = my_list.count(2)
print("Count of 2:", count_of_2)  # Output: 1

# 8. sort() - Sorts the list in ascending order (can be customized with key and reverse parameters)
my_list.sort()
print("After sort:", my_list)  # Output: [1, 2, 3, 4, 5]

# 9. reverse() - Reverses the elements of the list in place
my_list.reverse()
print("After reverse:", my_list)  # Output: [5, 4, 3, 2, 1]

# 10. copy() - Returns a shallow copy of the list
copied_list = my_list.copy()
print("Copied list:", copied_list)  # Output: [5, 4, 3, 2, 1]

# 11. clear() - Removes all elements from the list
my_list.clear()
print("After clear:", my_list)  # Output: []