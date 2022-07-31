
# pylint: disable=invalid-name

"""
@author: Shrikant Jagtap

This module covers below string functions:
	1. join(iterable): Returns the new concated string for given list or iterable.
	2. strip(char=" "):
	    It's used to remove leading and trailing white spaces and return new string.
	    If char provided then it's remove it.
	3. rstrip(char="#"): Returns new string by removing trailing white spces or specified chars.
	4. lstrip(char="@"): Returns new string by removing leading white spces or specified chars.

	5. replace(old_substring, new_substring, count=-1):
		old_substring: substring which need to replaced
		new_substring: substring which will replace old
		count: How many occurrence of old_string should be replaced.
		       default is -1 means replace all occurrences.

	6. swapcase(): Converts upper case string into lowercase and vice versa.
	7. title(): Returns new string with each world convert into titlecase.

	8. maketrans():
		1. If there is only one argument, it must be a dictionary mapping Unicode
		   ordinals (integers) or characters to Unicode ordinals, strings or None.
		      Character keys will be then converted to ordinals.

	        2. If there are two arguments, they must be strings of equal length, and
		   in the resulting dictionary, each character in x will be mapped to
		   the character at the same position in y.

	        3. If there is a third argument, it must be a string,
		   whose characters will be mapped to None in the result.

	9. translate(): Replace each characters in given string using above translation table.

	10. expandtabs(): Replace the tab characters \t with white spaces.
	                  We can provide tab size. default is 8.
	11.format_map(): Returns new formatted string with given mapping elements.

"""
first_name = "Sachin"
middle_name = "Ramesh"
last_name = "Tendulkar"

print("\n\n", "-" * 10, "str.join()", "-" * 10)
full_name = first_name + " " + middle_name + " " + last_name
print(full_name)

full_name = " ".join([first_name, middle_name, last_name])
print("Full Name with ' '.join() function: ", full_name)


full_name = "-".join([first_name, middle_name, last_name])
print("Full Name with '-'.join() function: ", full_name)

full_name = "#".join((first_name, middle_name, last_name))
print("Full Name with '#'.join() function: ", full_name)


# Strip function
print("\n\n", "-" * 10, "str.strip()", "-" * 10)
name = "   Sachin Ramesh Tendulkar   "
print(f"Before strip function: {name}")
print(f"After strip() function: {name.strip()}")

name = "$$$Sachin Ramesh Tendulkar$$$$"
print(f"\nBefore strip function: {name}")
print(f"After strip('$') function: {name.strip('$')}")

name = "rSachin Ramesh Tendulkar"
print(f"\nBefore strip function: {name}")
print(f"After strip('r') function: {name.strip('r')}")

# lstrip
print("\n\n", "-" * 10, "str.lstrip()", "-" * 10)
name = "rSachin Ramesh Tendulkar"
print(f"Before lstrip() function: {name}")
print(f"After lstrip('r') function: {name.lstrip('r')}")

# rstrip
print("\n\n", "-" * 10, "str.lstrip()", "-" * 10)
name = "Sachin Ramesh TendulkarS"
print(f"Before rstrip() function: {name}")
print(f"After rstrip('S') function: {name.rstrip('S')}")

print(name)


# replace
print("\n\n", "-" * 10, "str.replace()", "-" * 10)
name = "SacHin  RamesH Tendulkar"
new_name = name.replace("H", "h")
print(f"Replacing string for all occurrences: {new_name}")
new_name = name.replace("H", "h", 1)
print(f"Replacing string for 1 occurrence: {new_name}")


# swapcase
print("\n\n", "-" * 10, "str.swapcase()", "-" * 10)
name = "SacHin  RamesH Tendulkar"
print(f"Case1: After swapcase string: {name.swapcase()}")

name = "sachin  ramesh tendulkar"
print(f"Case2: After swapcase string: {name.swapcase()}")

name = "SACHIN  RAMESH TENDULKAR"
print(f"Case3: After swapcase string: {name.swapcase()}")

# title
print("\n\n", "-" * 10, "str.title()", "-" * 10)
name = "sachin  ramesh tendulkar"
print(f"convert into title string : {name.title()}")


# maketrans and translate functions

ds = {"a": "A", "s": "S", "l": "B"}

# case: 1
trans = name.maketrans(ds)
print("\n\n", "-" * 10, "str.maketrans() and str.translate()", "-" * 10)
print("Case : 1")
print("Created mapping table using maketrans(): ", trans)

translated_string = name.translate(trans)

print("Translated string using mapping table: ", translated_string)

# case : 2
trans = name.maketrans("asl", "ASB")
print("\nCase : 2")
print("Created mapping table using maketrans(): ", trans)
print("Translated string using mapping table: ", name.translate(trans))

# case: 3
trans = name.maketrans("asl", "ASB", "dr")
print("\nCase : 3")
print("Created mapping table using maketrans(): ", trans)
print("Translated string using mapping table: ", name.translate(trans))


mp = {97: 65, 115: 83, 108: 66, 100: None, 114: None}
print("\nCase : 4")
print(
    f"You can create unicode dict like: {mp} and use it direct in translate function: "
)
print("Translated string using unicode mapping dict: ", name.translate(mp))


# expandtabs
print("\n\n", "-" * 10, "str.expandtabs", "-" * 10)
message = "hello\tpython\tbye\t"
print("Expandtabs without tabsize(default is : 8", message)
print("Expandtabs with tabsize=20", message.expandtabs(tabsize=20))
print("Expandtabs with tabsize=1", message.expandtabs(tabsize=20))

# format_map
print("\n\n", "-" * 10, "str.format_map", "-" * 10)
mp = {"name": "Ganesh"}
message = "Hello {name}"
print("format_map :", message.format_map(mp))


message = "value of {a} is {b}"
print("format_map :", message.format_map({"a": "Python", "b": "100"}))
print("format : ", message.format(a="Python", b="100"))
print("format : ", message.format(**{"a": "Python", "b": "100"}))
