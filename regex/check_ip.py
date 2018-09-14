"""
    Extract ip address from string
"""

import re

string = """216.3.128.90
            An IP address is written in "dotted decimal" notation,
            which is 4 sets of numbers separated by period each set
            representing 8-bit number ranging from (0-255).
            An example of IPv4 address is 216.3.128.12,
            which is the IP address previously assigned to iplocation.net.
         """

pattern = re.compile("\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}",
                     re.IGNORECASE)

matches = re.findall(pattern, string)

if matches:
    print(*matches)
else:
    print("No IP found")

# re.match() : returns match object if pattern matches at begining of string
# re.search() : searches string pattern in whole string, return first searches
# re.findall(): return all occurrences of matched string
