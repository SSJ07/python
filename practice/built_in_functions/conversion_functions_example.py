'''
Created on Jan 12, 2018

@author: shrikant_jagtap
        
        
        char()
        int()
        float()
        bool()
        list()
        set()
        dict()
        hex()
        bin()
        oct()
        ord()

'''

'''
    chr() : function converts any value into character
'''
ch = chr(65)
print("char value of 10 is :{}".format(ch))

'''
    int() function converts any value into integer
'''
integer = int("10")
print("integer value of 10 is :{}".format(integer))

'''
    float() function converts any value into fraction type value
'''
flt = float("10.10")
print("float value of 10 is :{}".format(flt))

'''
    bool() function converts any value into boolean value
'''
bol = bool("10.10")
print("boolean value of 10.10 is :{}".format(bol))
bol = bool("")
print("boolean value of empty string is :{}".format(bol))

'''
    list() converts any iterable set of elements into list
'''
ls = list(range(10))
print("list of 1 to 10 numbers is :{}".format(ls))
ls = list({1,2,3,4,5,6,7,8,9,10})
print("list of 1 to 10 numbers is :{}".format(ls))

'''
    set() converts iterable values into unique set
'''
    
ls = set([1,2,2,3,4,5,5,6,6,7,8,9])
print("set of unique elements is :{}".format(ls))


'''
    dict() function converts into dictionary
'''
ls  = dict(zip(ls,ls))
print("dictionary is :{}".format(ls))

'''
    ord() function converts character value to it's integer value. 
    It takes single character.
'''
print("integer value of '{}' is {}".format('a', ord('a')))
print("integer value of '{}' is {}".format('A', ord('A')))


'''
    bin() function converts integer value to binary representation.
    It takes integer value as parameter.
'''
print("binary representation of {} is {}".format(10, bin(10)))
print("binary representation of {} is {}".format(15, bin(15)[2:]))

'''
    hex() function converts integer value into hexadecimal representation.
'''
print("hex decimal representation of {} is {}".format(15, hex(15)))
print("hex decimal representation of {} is {}".format(35, hex(35)))


'''
    oct() function converts integer value into octal representation
'''
print("hex decimal representation of {} is {}".format(10, oct(10)))
print("octal representation of {} is {}".format(35, oct(35)))



