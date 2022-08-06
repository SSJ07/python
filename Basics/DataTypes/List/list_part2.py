"""
	List operations:
		1. slicing
		2. indexing
		3. append(new_value)
		4. insert(position, new_value)
		5. remove(value): Raise KeyError if value not found
		6. pop(): Removes last item from list
		7. clear(): Removes all items from list
		8. reverse()
		9. sort()
"""

list_of_numbers = [1, 2, 3, 4]
print("Initial list: ", list_of_numbers)
print(list_of_numbers)

list_of_numbers[1] = "Changed value"
print("After changing the list: ", list_of_numbers)
print(list_of_numbers)

print("After changing the list using slicing: ", list_of_numbers)
list_of_numbers[1:3] = [0, 0]
print(list_of_numbers)


list_of_numbers.append(5)
print("After appending item to the list using append: ", list_of_numbers)
print(list_of_numbers)


list_of_numbers.insert(0, 0)
print("After inserting item to 0th position using insert: ", list_of_numbers)
print(list_of_numbers)

list_of_numbers.insert(0, -1)
print(list_of_numbers)

# deleting the particular number
print("-" * 10, "delete item from list", "-" * 10)
del list_of_numbers[0]
print(list_of_numbers)

list_of_numbers.remove(0)
print(list_of_numbers)
list_of_numbers.remove(0)
print(list_of_numbers)
list_of_numbers.remove(0)
print(list_of_numbers)

# clear the whole list
# list_of_numbers.clear()
# print(list_of_numbers)


# pop item from the list
list_of_numbers.pop()
print(list_of_numbers)
list_of_numbers.pop()
print(list_of_numbers)
list_of_numbers.pop()
print(list_of_numbers)

# reverse()
print("-" * 10, "revers the list", "-" * 10)
ls = [3, 1, 0]
ls.reverse()
print(ls)
ls.reverse()
print(ls)

# sort()
print("-" * 10, "sort the list", "-" * 10)
ls = [4, 3, 1, 0, 5, 7, 10]
print("Before the sort", ls)
ls.sort()
print(ls)

ls = [4, 3, 1, 0, 5, 7, 10]
print("Before the sort", ls)
ls.sort(reverse=True)
print(ls)


# operations on list
# +, *

ls = [1, 2]
ls_2 = [2, 3, 4]

ls_3 = ls + ls_2
print(ls_3)

ls_4 = [1] * 10
print(ls_4)
