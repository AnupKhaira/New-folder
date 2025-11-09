x = frozenset([1,2,3,4,5])
y = frozenset([3,4,5,6,7])

print(x.isdisjointy(y))
print(x.difference(y))
print(x | y)