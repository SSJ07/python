"""
	Set:
		1. Unique items(No duplicates)
		2. Unordered:
			1. Not supports: indexing and slicing
		3. mutable OR we can the set
			1. Items should be a immutable like: int, string, tuple
			2. list, set, and dict can't insert into a set
		4. Set support some math operations


	Set creation:
		 1. {}
		 2. set

"""

# create set using {}: 1
set_of_num = {1,2,3,4,5}
print("Python set", set_of_num)
print("Python type of set", type(set_of_num))

# create set using 'set' class
set_of_num = set([1,2,3,4,5, 3,4,5])
print("Python set", set_of_num)
print("Python type of set", type(set_of_num))

set_of_string = set("Hello Python")
print("Python set", set_of_string)
print("Python type of set", type(set_of_string))


# Operations:
#	1. add/update
#	2. removing items


set_of_string.add("New Value")
print("After adding new item to set: ", set_of_string)

#set_of_string.add(["New Value", "Value new", "123"])
#print("After adding new item to set: ", set_of_string)

# update()
print("-"*10, "set.update", "-"*10)
set_of_string.update(["New Value", "Value new", "123"])
print("After updating the set: ", set_of_string)

set_of_string.update("add new string as update")
print("After updating the set: ", set_of_string)

# Removing item
# 1. discard
# 2. remove


set_of_string.discard("New Value")
print("After discarding item from set:", set_of_string)

set_of_string.discard("sjdfjslfslkdlf")
print("After discarding item from set:", set_of_string)

# remove()
set_of_string.remove("P")
print("After removing item from set:", set_of_string)

#set_of_string.remove("sjdfjslfslkdlf")
#print("After removing item from set:", set_of_string)

# pop()
print("Set before pop: ", set_of_string)
set_of_string.pop()
print("Set after pop single item: ", set_of_string)

#new_set = {}
#new_set.pop()
#print("Set after pop single item: ", set_of_string)

# clear
set_of_string.clear()
print("After clear() the set:", set_of_string)
