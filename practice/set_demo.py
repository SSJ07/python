##we can create set using set()
## set doesn't allow duplicates

set_demo = set()
for i in range(10):
    set_demo.add(i)
## add duplicates to set
set_demo.add(1)
set_demo.add(2)
print(set_demo)

## we can convert list into set using set(list)

ls = [ x for x in range(1,11)]
set1 = set(ls)
print(set1)
