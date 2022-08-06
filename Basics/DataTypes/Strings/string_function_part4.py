"""
@author: Shrikant Jagtap

This module covers below string functions:
	1.isalnum(): Returns True if it’s made of alphanumeric characters only.
	2.isalpha():
	  Returns True if all the characters in the string are alphabets, otherwise False.
	3.isdecimal():
	  Returns True if all the characters in the string are decimal characters, otherwise False.
	4.isdigit():
	  Returns True if all the characters in the string are digits, otherwise False.
	5.isidentifier():
	  Returns True if the string is a valid identifier according to the Python language definition.
	6.isnumeric():
	  Returns True if all the characters in the string are numeric, otherwise False.
	  If the string is empty, then this function returns False.
	7.isprintable():
	  Returns True if all characters in the string are printable or the string is empty,
	  False otherwise.
	8.isspace():
	  True if there are only whitespace characters in the string, otherwise it returns False.
	9.istitle():
	  True if the string is title cased and not empty, otherwise it returns False.
	10. ljust():
	  Adjust string left justified with given char.
	11. rjust():
	  Adjust string right justified with given char.

"""
# pylint: disable=invalid-name

example = "Code24"
print("isalnum(): ", example.isalnum())

example = "Code24 "
print("isalnum(): ", example.isalnum())

example = "Code24i\n"
print("isalnum(): ", example.isalnum())

example = "Code"
print("isalnum(): ", example.isalnum())
print("isalpha(): ", example.isalpha())

example = "100"
print("isalnum(): ", example.isalnum())
print("isalpha(): ", example.isalpha())

# isdecimal
print("isdecimal(): ", example.isdecimal())
print("isdecimal(): ", "A".isdecimal())
print("isdecimal(): ", "B".isdecimal())
print("isdecimal(): ", "b101".isdecimal())

#  isdigit
print("isdigit(): ", "101".isdigit())
print("isdigit(): ", "A123213".isdigit())
print("isdigit(): ", "101".isdigit())
print("isdigit(): ", "101 ".isdigit())

# isidentifier
message = "$message"
print("isidentifier: ", message.isidentifier())

message = "_message"
print("isidentifier: ", message.isidentifier())

message = "10message"
print("isidentifier: ", message.isidentifier())

#  isnumeric
print("isnumeric(): ", "101".isnumeric())
print("isnumeric(): ", "A123213".isnumeric())
print("isnumeric(): ", "10123131".isnumeric())

# isprintable
print("\t".isprintable())
print("\n".isprintable())
print("message".isprintable())
print("100".isprintable())

# isspace
print("-"*10, "str.isspace", "-"*10)
print(" ".isspace())
print("                             ".isspace())
print(" hello".isspace())
print(" hello ".isspace())
print(" hello python ".isspace())

print("-"*10, "str.istitle", "-"*10)
print("hello".istitle())
print("Hello python".istitle())
print("Hello Python".istitle())
print("".istitle())

print("-"*10, "str.ljust", "-"*10)
print("hello".ljust(50))
print("hello".ljust(70, "-"))
print("hello".ljust(100, "*"))

print("-"*10, "str.rjust", "-"*10)
print("hello".rjust(50))
print("hello".rjust(70, "-"))
print("hello".rjust(100, "*"))
