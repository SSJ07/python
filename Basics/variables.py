'''
Created on Feb 6, 2018

@author: Shri
'''

'''
    Python is loosly typed language.
    It allows any type data to assign variable.
    Python support mainly two types of variables:
            1: Number :
                    a) integer
                    b) floating
            2. String
            3. Boolean
'''

a = 10
print("Integer value a={}".format(a))

b = 10.30
print("floating value b={}".format(b))


name = "python"
print("string value name={}".format(name))

'''
    python integer value doesn't have limit
'''
c = 243423423847237444444444444444444441274127892738913271892739812789273981273891273891273891273891273981329713891238
print("unlimited integer value c={}".format(c))


'''
    convert other value into integer
    by using int("10 base value")
'''
val = int("10")
print("string to integer val={}".format(val))

'''
    convert string to float
'''
val = float("10.20")
print("string to float val={}".format(val))

'''
    use str() to convert int to string
'''
val = str(10)
print("integer to string val={}".format(val))

boolean = True

if boolean:
    print("THis is true")
