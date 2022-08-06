# Set operations
# 1.Union
# 2.intersection
#.3 symmetric difference
#.4 difference
"""
## Other methods:
      1. intersection_update()
      2. symmetric_difference_update()
      3. issubset(): True if this is part of another set else False
      4. issuperset(): True if contains another set else False
      5. isdisjoint(): True if not found any common items else False
"""

set_A = {1,2,3,4,5, 100}
set_B = {4,5,6,7,8}


# union()
# |

set_c = set_A | set_B
print(set_c)

set_d = set_A.union(set_B)
print("set_d :", set_d)
print("set_A:", set_A)
print("set_B:", set_B)


# intersection()
# &
print("common items from set_A and set_B: ", set_A.intersection(set_B))
print("common items from set_A and set_B using &: ", set_A & set_B)

# symmetric_difference()
# ^
print("symmetric difference: from set_A and set_B: ", set_A.symmetric_difference(set_B))
print("symmetric difference: from set_A and set_B: ", set_A ^ set_B)

# difference()
# -
print("difference: from set_A: ", set_A.difference(set_B))
print("difference: from set_A: ", set_A - set_B)

print("difference: from set_B: ", set_B.difference(set_A))
print("difference: from set_B: ", set_B - set_A)

# intersection_update()
#set_B.intersection_update(set_A)
#print("After intersection_update: ", set_A)
#print("After intersection_update: ", set_B)


# intersection_update()
set_A.symmetric_difference_update(set_B)
print("After symmetric difference udpate: ", set_A)
print("After symmetric difference udpate: ", set_B)

set_C = {1,2, 100}
print("set_C is subset of setA?: ", set_C.issubset(set_A))
print("set_A is superset of set_C?: ", set_A.issuperset(set_C))

set_D = {1,2,3, 4}
set_E = {4,5,6}
print("is set_D disjoint to set_E?: ", set_D.isdisjoint(set_E))
print("is set_E disjoint to set_D?: ", set_E.isdisjoint(set_D))


#frozenset

fs = frozenset([1,2,3,4,5])
print(fs)
# fs.add(100) <--- Can't add item to frozenset
