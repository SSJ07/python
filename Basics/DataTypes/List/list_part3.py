"""
@author: Shrikant Jagtap

List in python
	1. extend
	2. copy
	3. count

	4. list comprehension

"""
# pylint: disable=unnecessary-comprehension

numbers = [1, 2, 3, 4, 5]
other_numbers = [6, 7, 8, 9, 10]

numbers.append(other_numbers)
print(numbers)

# extend
numbers.extend(other_numbers)
print(numbers)


# copy
even_numbers = [2, 4, 6]
evn_numbers1 = even_numbers

print(even_numbers)
print(evn_numbers1)

evn_numbers1.append(8)
print("Afte modifying the list")
print(even_numbers)
print(evn_numbers1)

print("ID of numbers is : ", id(numbers))
print(id(even_numbers))
print(id(evn_numbers1))


evn_numbers2 = evn_numbers1.copy()
print("ID of evn_numbers2 is :", id(evn_numbers2))
print("env_numbers2:", evn_numbers2)


evn_numbers2.extend([2, 4, 8, 10])
print(evn_numbers2)
print(evn_numbers2.count(2))

ls_comp_example = [x for x in range(10)]
print(ls_comp_example)

str_list = list("abcdedf")
print(str_list)
str_list = list((1, 2, 4, 4, 55))
print(str_list)
