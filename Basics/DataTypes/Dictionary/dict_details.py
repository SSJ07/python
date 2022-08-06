"""
@author: Shrikant Jagtap

Dictionary:
	1. It's data type holds data in key-value pairs
	2. Unordered
	3. Key should be immutable
	4. Value can retrieve using key
Creation of Dictionary:
	1. using {}
	2. using dict class
Dictionary methods:
	1. get(key): Accessing the value for particular key
	2. update(dict/iterable)
	3. delete items from dict:
		1. popitem()
		2. pop(key)
		3. clear()
		4. del
	4. keys():
	5. values()
	6. copy() vs deepcopy()
	7. items()
	8. fromkeys()

Dict comprehension
collections module:
	OrderedDict
	Defaultdict
"""

from copy import deepcopy

# creation of dict
print("-"* 10 , "dict creation", "-"*10)
print("-"* 5, "Using {}", "-"*10)
ds = {"python": 80, "java": 78}
print(ds)
print(type(ds))

print("-"* 5, "Using dict(List[tuple(key, value)])", "-"*10)
ds1  = dict([("python", 80), ("java", 80)])
print(ds1)
print(type(ds1))

print("-"* 5, "Using dict(tuple(tuple(key, value)))", "-"*10)
ds2 = dict((("python", 80), ("java", 80)))
print(ds2)
print(type(ds2))

print("-"* 10 , "Adding new key,value to dict", "-"*10)
ds2["DevOps"] = 90
print(ds2)

print("-"* 10 , "Replacing key,value to dict", "-"*10)
ds2["python"] = 70
print(ds2)

print("-"* 10 , "Updating dict with new dict/iterable", "-"*10)
ds_new = {"javascript": 86, "terraform": 78}
ds2.update(ds_new)
print("After using update function: ", ds2)

ds2.update([("python", 10), ("java", 20)])
print(ds2)

# using keys to get values
print("-"* 10 , "Retrieving value from dict using key", "-"*10)
ds_new = {"javascript": 86, "terraform": 78}
print("-"*100)
print("value of 'python' key is: ", ds2["python"])
print("value of 'python' using get(): ", ds2.get("java"))

#print("value of python key", ds2["Linux"])
print("value of python using get", ds2.get("Linux"))

# delete operation
print("-"* 10 , "Deleting items from dict", "-"*10)
print("Before popitem from ds2:", ds2)
response = ds2.popitem()
print("After popitem from ds2:", ds2, response)

# pop
rsp = ds2.pop("python")
print("pop python item from ds2:",ds2, rsp)

#new_ds = {}
#new_ds.popitem()
#ds2.pop("Git")
#del ds2["javaa"]
#print("after using del :", ds2)
print("All keys of ds2: ", ds2.keys())
print("All values of ds2:", ds2.values())

print("-"*100)
ls = [80, 90, 45]
ds_new = {"python": ls, "java": [67, 87, 65]}
print(ds_new)
ds_new_1 = deepcopy(ds_new)
print(ds_new_1)

ls.append(100)
print(ds_new)
print(ds_new_1)
ds_new_1 = ds_new.copy()
ds_new_1 = ds_new.copy()

new_ds2 = ds2.fromkeys(range(100))
print(new_ds2)

# dict comprehension
ds = {x: x*x for x in range(1,11)}
print(ds)
