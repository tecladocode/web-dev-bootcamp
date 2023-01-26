# this is a list - you can add & subtract elements - it is ordered and mutable
l = ["Michelle", "PK", "Milo"]

# this is a tuple - you CANNOT add or subtract elements - it is ordered and immutable
t = ("Michelle", "PK", "Milo")

# this is a set - you can add & subtract elements but CANNOT have dupes - the order isn't guaranteed and it is mutable
s = {"Michelle", "PK", "Milo"}

# elements in lists and tuples can be accessed by bracket or subscript notation
print(l[2])

# because sets don't have a guaranteed order, it does not make sense to use bracket or subscript notation on them

# of course, there are different methods for lists, tuples and strings - some examples:
l.append("Ferris")
print(l)

s.add("Baby")
print(s)
