
# pylint: disable=invalid-name

"""
@author: Shrikant Jagtap

This module demostrate how string slicing works.
	1. String slicing always return substring
	2. String slicing use [] brackets to slice string
	3. String slice follows [start: end: step] pattern
		1. start: Index of substring to start slicing
		2. stop: Index of substring till where have to slicing
		3. step: Increment of characters in slice
	4. below are some combinations of slicing:
		1. [:] -> No start and end means complete string.
		2. [start:] -> Start and no end means complete string from given strart index.
		3. [:end] -> No start but given end means complete string between 0th index to end index.
		4. [start: end] -> substring between start and end
	5. String slicing support both positive and negative indexing
"""
# String slicing


message = "python is a very popular language"

print("\n", "-" * 10, "String slicing", "-" * 10)
print('message = "python is a very popular language"')
slice_part = message[12:16]
print("message[12:16] :", slice_part)

# [start: stop: step]

slice_part_2 = message[12:16:2]
print("message[12:16:2]: ", slice_part_2)


# alternate character string

alternate_char = message[::3]
print("message[::3]: ", alternate_char)


# print only python substring

python_substring = message[:6]
print("message[:6] :", python_substring)


sub_string = message[10::2]
print("message[10::2] :", sub_string)


# Negative indexing with slicing

reverse_string = message[::-1]
print("message[::-1] :", reverse_string)


negative_slice = message[16:11:-1]
print("message[16:11:-1] : ", negative_slice)
