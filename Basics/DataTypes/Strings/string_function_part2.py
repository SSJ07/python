"""
@author : Shrikant Jagtap

This moduel covers below string functions:
	1. split(sep='char', maxsplit=number):
		1. sep: We can provide separator to split string. e.g: '-'
		2. maxsplit: split string into number of parts.
	2. rsplit(): split string right to left
	3. splitlines(): split string with \n escape characters.
	4. partition(sep='char'): similar like split but sep is mandatory param
		and alwys returns tuple of three parts(first part, sep, second part)
	5. rpartition(): similar like partition but it partition string right to left.
"""

FULL_NAME = "Sachin Ramesh Tendulkar"

# split function with no arguments default space
(
    first_name,
    middle_name,
    last_name,
) = FULL_NAME.split()  # ["Sachin", "Ramesh", "Tendulkar"]
print("\n", "-"*10, "str.split", "-"*10)
print(f"First Name: {first_name}")
print(f"Middle Name: {middle_name}")
print(f"Last Name: {last_name}")


WEEKDAYS = "Monday-Tuesday-Wednesday-thursday-Friday"
WEEKDAYS_ls = WEEKDAYS.split(
    "-"
)  # ["Monday", "Tuesday", "Wednesday", "thursday", "Friday"]
print("string with '-': ", WEEKDAYS_ls)


monday = WEEKDAYS.split(
    "-", maxsplit=1
)  # ["Monday", "Tuesday-Wednesday-thursday-Friday"]
print("string with '-' and maxsplit=1", monday)


FULL_NAME_WITH_SPACES = "Sachin      Ramesh       Tendulkar"
print("string with default white spaces: ", FULL_NAME_WITH_SPACES.split())


# rsplit
print("\n\n", "-"*10, "str.rsplit", "-"*10)
print(
    "rsplit with sep and maxsplit :",
    FULL_NAME_WITH_SPACES.rsplit(sep=" ", maxsplit=1),
)


# splitlines
print("\n\n", "-"*10, "str.splitlines", "-"*10)
MESSAGE = "Hello\nPython\nGood\nBye\n"
print("splitlines : ", MESSAGE.splitlines())
print("splitlines with keepends=True: ", MESSAGE.splitlines(keepends=True))
print(MESSAGE.split("\n"))


# partition
print("\n\n", "-"*10, "str.partition", "-"*10)
print("partition string : ", FULL_NAME.partition(" "))
print("partition string with 'sh': ", FULL_NAME.partition("sh"))

# rpartition
print("\n\n", "-"*10, "str.rpartition", "-"*10)
print("rpartition string :", FULL_NAME.rpartition(" "))
print("rpartition string with 'sh'", FULL_NAME.rpartition("sh"))
