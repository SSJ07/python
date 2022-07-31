"""
@author: Shrikant Jagtap

This module demostrate string formatting with following options:

	1. C-style formatting:
		1. %d - digit
		2. %c - character
		3. %x - hexadecimal
		4. %f - float
	2. .format() function
	3. f-string
	4. String templating
"""
from string import Template


print("\n\n", "-" * 10, "C-style formatting", "-" * 10)
print(
    "'%s'%('Hello Python')=", "%s" % ("Hello Python") # pylint: disable=consider-using-f-string
)
print('"%s"%(100)=', "%s" % (100))  # pylint: disable=consider-using-f-string
print('"%d"%(1001)=', "%s" % (1001))  # pylint: disable=consider-using-f-string
# print("%d"%("Hello python"))


print("%c" % (65))  # pylint: disable=consider-using-f-string
print("%3.4f" % (3.455666))  # pylint: disable=consider-using-f-string
print("%x" % (15))  # pylint: disable=consider-using-f-string
print("%x" % (10))  # pylint: disable=consider-using-f-string


# .format function

URL = "https://google.com/api/{part}"


MESSAGE = "Hello, {NAME}"
print("\n\n", "-" * 10, ".format()", "-" * 10)
print("MESSAGE = Hello, {NAME}")
print('MESSAGE.format(NAME="Python"): ', MESSAGE.format(NAME="Python"))
print('MESSAGE.format(NAME="Java"): ', MESSAGE.format(NAME="Java"))
print('MESSAGE.format(NAME="C")', MESSAGE.format(NAME="C"))
print('MESSAGE.format(NAME="DevOps")', MESSAGE.format(NAME="DevOps"))
print('MESSAGE.format(NAME="Javascript")', MESSAGE.format(NAME="Javascript"))


MESSAGE = "{1}, How are you?. Today is {0}"
print("{1}, How are you?. Today is {0}: ", MESSAGE.format("Jhon", "Friday"))


# f-string

print("\n\n", "-" * 10, ".f-string()", "-" * 10)
DATA_TYPE = "Good"

MESSAGE = f"Python is very {DATA_TYPE} languAGE"
print('f"Python is very {DATA_TYPE} languAGE": ', MESSAGE)

NAME = "Jhon"
AGE = 25
MESSAGE = f"{NAME=}, {AGE=}"
print('f"{NAME=}, {AGE=}": ', MESSAGE)


print("\n\n", "-" * 10, ".string.Template class", "-" * 10)

temp = Template("Hello ${NAME}")
print("temp = Hello ${NAME}")
print('temp.substitute(NAME="Ram"): ', temp.substitute(NAME="Ram"))
