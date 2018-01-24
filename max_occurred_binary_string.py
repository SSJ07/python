'''
  It counts maximum occurrences of '1'  substring in given string.
  example: if string is '11011' then output will be 2
'''


n = int(input().strip())
ls = format(n, 'b').split("0")
print(len(max(ls)))
