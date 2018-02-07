'''
@author: shri
'''

string = "python is very popular language"

print(string)

''' split string into list of tokens'''

tokens = string.split(" ")

print("all tokens are :{}".format(tokens))

''' iterate over string using for loop'''
for i in string:
    print(i,end=" ")
print("\n")

'''access substring using indices'''

print("substring from 0 to 6 is : {}".format(string[0:6]))

''' print alternate character in string '''
print("alternate char string : {}".format(string[0::2]))

''' print reverse string using indices'''
print("reverse string is : {}".format(string[::-1]))

''' count the total vowels in string'''
count = sum(1 for x in string if x in ['a', 'e','i','o', 'u'])
print("total vowels in string is: {}".format(count))

''' print length of string '''
print("length of string is : {}".format(len(string)))

''' join list of tokens into string '''
join_string = " ".join(tokens)
print("joined string is : {}".format(join_string))

''' count specific char in string '''
print("total number of {} in {} is :{}".format('a', string, string.count('a')))
