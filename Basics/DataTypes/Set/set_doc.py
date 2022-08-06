"""
@author: Shrikant Jagtap

Set:
	Set is collection of unique elements.
	1. Unordered
	2. Indexing and slicing does not supports
	3. Unique(No duplicates)
	4. Set is mutable(we can change it)
	5. But item should be immutable(What if we try to insert mutable values in it?)
	6. Support mathamatical operations
		1. union
		2. intersection
		3. symmetric difference

	Set creation:
		{}
		set()

       Methods of set class:
       		## Adding elements
       			1. add(value): value -> int,tuple, string
			2. update(iterable): iterable -> list, set, dict, string, tuple
		## Removing elements:
			1. discard(item): Remove if item is present else do nothing
			2. remove(item): Remove if item is present else raise KeyError
			3. pop(): removes and returns item. Raise KeyError
			4. clear(): removes all items from set.
		## Set Operations:
			1. union:
				1. Combines all items from both sets. merge duplicates
				2. | or set_A.union(set_B)
			2. intersection:
				1. Returns common items from both sets.
				2. & or set_A.intersection(set_B)
			3. difference:
				1. Returns uncommon items from first set.
				2. - OR set_A.difference(set_B) -> unique item from set_A but not in set_B
			4. symmetric difference:
				1. Returns uncommon items from both sets.
				2. ^ OR set_A.symmetric_difference(set_B)

	      ## Other methods:
	      		1. intersection_update()
			2. symmetric_difference_update()
			3. issubset(): True if this is part of another set else False
			4. issuperset(): True if contains another set else False
			5. isdisjoint(): True if not found any common items else False
"""
