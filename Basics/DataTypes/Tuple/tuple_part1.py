"""
Tuple:
	1. Tuple itself is immutable but values inside tuple may mutable
	2. We can use indexing and slicing
	3. Ordered
	4. Can have duplicates

	tuple creation:
		1. (value1,value2). Only one value in () not create tuple. E.g: (10) <-- this is not tuple
		2. tuple(iterable)
		3. comma separated values. E.g: value1,value2,

	methods of tuple:
		1. count(): Returns the count of given value
		2. index(): Raise exception if value not present in tuple
	Other operations:
		1. tuple concatenation
		2. mutiplication (value1,)*10 <---- This will create tuple of value1 with 10 time repetation

"""
# pylint: disable=trailing-comma-tuple

print("\n", "-"*10, "tuple creation", "-"*10)
print("Case1: using ()")
num_tp = (1,2,3,2,3, 4,5)
print(num_tp)
print(type(num_tp))

#num_tp[2] = 100
#print(num_tp)

print("\n", "-"*10, "Tuple Inexing", "-"*10)
print("0th position value: ", num_tp[0])
print("1th position value: ", num_tp[1])

print("\n", "-"*10, "Tuple Negative Inexing", "-"*10)
print("-1th position value: ", num_tp[-1])
print("-2th position value: ", num_tp[-2])

# slicing
print("\n", "-"*10, "Tuple slicing", "-"*10)
print("slice [0:3]: ", num_tp[0:3])

tp1 = (1,2)
tp2 = (3,4)
print("\n", "-"*10, "Tuple concatenation", "-"*10)
print("Tuple concatenation tp1+tp2: ", tp1+tp2)

print("\n", "-"*10, "Tuple creation using * operator: (1,)*100", "-"*10)
tp_of_1 = (1,)*100
print(tp_of_1)


print("\n", "-"*10, "Tuple creation using comma separator: 1,", "-"*10)
tp_of_1 = 1,
print(tp_of_1, type(tp_of_1))

print("\n", "-"*10, "Tuple creation with different data type: 1,", "-"*10)
tp_of_mix_value = (1, "hello", [1,2,3,4])
print(tp_of_mix_value)
print("After changing item in tuple: append value to list:")
tp_of_mix_value[2].append(100)
print(tp_of_mix_value)

print("After changing item in tuple: replacing string: Immutable: no change:")
tp_of_mix_value[1].replace('e', "E")
print(tp_of_mix_value)


# tuple functions
# count
# index

print("Count of 2 : ", num_tp.count(2))
print("Count of 100 : ", num_tp.count(100))

print("index of 2 : ", num_tp.index(2))
print("Try to get index of non member value of tuple: Will raise Exception")
print("index of 100 : ", num_tp.index(100))
