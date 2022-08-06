"""
	List Data type:
		1. Ordered
		2. Can have duplicates
		3. Mutable/can modify it
"""
# pylint: disable=invalid-name
# pylint: disable=unnecessary-comprehension

# syntax or declaration of list

list_of_numbers = [1, 2, 3, 4, 5]
print(list_of_numbers)
print(type(list_of_numbers))

# get the element from list using positive index
first_item = list_of_numbers[0]
print(first_item)
fourth_item = list_of_numbers[3]
print(fourth_item)
# seventh_item = list_of_numbers[6]
# print(seventh_item)

# get the element from list using negative index
print("-" * 10, "list negative indexing", "-" * 10)
last_item = list_of_numbers[-1]
print(last_item)
sl_item = list_of_numbers[-2]
print(sl_item)
# six_item = list_of_numbers[-6]

# slicing of list
# [start: stop: step]
print("-" * 10, "list slicing", "-" * 10)
list_of_even_numbers = [x for x in range(100) if x % 2 == 0]
print(list_of_even_numbers)
first_ten_even_numbers = list_of_even_numbers[1:11]
print(first_ten_even_numbers)

alternate_numbers = list_of_even_numbers[1:21:2]
print(alternate_numbers)

first_number = list_of_even_numbers[0:1]
print(first_number)


# list of strings
print("-" * 10, "list types", "-" * 10)
list_of_skills = ["Python", "DevOps", "Java", "Git", "Unix", "Terraform"]

print(list_of_skills)
