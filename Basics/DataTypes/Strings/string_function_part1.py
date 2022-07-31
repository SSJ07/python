"""
@author: Shrikant Jagtap

This module demostrate how to use following functions of string in python:
	1. capitalize(): Convert first character in upper case letter.
	2. casefold(): Convert whole string into lower case.
	3. lower(): Convert whole string into lower case. Subset of casefold().
		    casefold() support all unicode characters.
	4. center(width, fillchar=' '):
		Padding the string at center by filling provided char with that width.
	5. count(substring, start, end):
		Count the occurrences of substring in the given string
		between start and end index.
		start and end parameters are optional.
	6. encode(): convert string into bytes
	7. endswith(substring):
		Check given substring appears at the end or not.
		Returns True if endswith given substring otherwise False
	8. startswith(substring):
		Check given substring appears at the begining or not.
		Returns True if startwith given substring otherwise False

"""
# capitalize()
MESSAGE = "hello python"
CAPITALIZED_MESSAGE = MESSAGE.capitalize()
print("capitalize() : ", CAPITALIZED_MESSAGE)  # output: "Hello python"

# casefold()
MESSAGE = "HELLO PythoN HELLO"
print("casefold(): ", MESSAGE.casefold())  # output: hello python hello

# lower()
print("lower():", MESSAGE.lower())  # output: hello python hello

# center()
print(
    "center():", MESSAGE.center(50, "=")
)  # output: ===================HELLO PythoN HELLO===================


# count() function
print(f"count of 'ythoN' = {MESSAGE.count('ythoN')}")  # output: 1
print(f"count of 'ythonn' = {MESSAGE.count('ythonn')}")  # output: 0

# encode
MSG = MESSAGE.encode("utf-8")
print("encoded string: ", MSG)


# endswith
FILES_EXTENSION = "demo.py"
print(f"file {FILES_EXTENSION} ends with .py? : {FILES_EXTENSION.endswith('.py')}")
print(f"file {FILES_EXTENSION} ends with .xml? : {FILES_EXTENSION.endswith('.xml')}")


# startswith
print("startswith : demo? : ", FILES_EXTENSION.startswith("demo"))
print("startswith : string_? : ", FILES_EXTENSION.startswith("string_"))


# find
print(f"Is 'python' in string? : {MESSAGE.find('Python')}")
print(f"Is 'HELLO' in string? : {MESSAGE.find('HELLO')}")
print(f"Is 'O' in string? : {MESSAGE.find('O')}")


# upper() : It converts string into upper case letters

print("upper case string: ", MESSAGE.find("hello".upper()))

# find() : returns index of substring if substring found else returns -1
print("find 'hello' in string: ", MESSAGE.find("hello"))


# index(): Returns index of given substring if it present in string else throw exception

print("Use index function: ", MESSAGE.index("N", 0, 15))


# islower(): Check the whole string is lowercase or not

print(f"{MESSAGE} is lower string?", MESSAGE.lower().islower())


# isupper() : Check the whole string is upper case or not

print(f"{MESSAGE} is uppper string?", MESSAGE.upper().isupper())

# lower() : Returns new string with lower case letters.
RESULT = MESSAGE.lower()
print("RESULT: ", RESULT)
print("is lower?", RESULT.islower())
