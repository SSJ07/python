string = """
            Git tells you the two files that have changed. In this case, 
            These are the compared files. There is an A version, and a B version. 
            There are instances where version A and B are two different files, 
            but in most cases they are the same. To be sure, 
            Git will always define what file represents item A or B.
            """
            
reg_ex = re.compile(r"Git|file")
matches = reg_ex.findall(string)
if matches:
    print(*matches)
else:
    print("No string matches found")
