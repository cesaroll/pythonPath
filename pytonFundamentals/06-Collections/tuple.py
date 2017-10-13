#
t = ("Norway", 4.967, 3)
print(t)
print(t[0])

for item in t:
    print(item)

print(t + (338116.0, 265e9))

print(t)

a = ((220,284), (454,6765), (23,45))
print(a)
print(a[2])
print(a[2][1])

print("\nSingle item tuple")
t = (4)
print(type(t))
t = (4,)
print(type(t))

print("\nEmpty Tuple")
t = ()
print(type(t))


print("\nFunction returning several tuple variables")

def minmax(items):
    print(items)
    return min(items), max(items)


lower, upper = minmax([83, 33, 84, 32, 85, 31, 86])
print("\nLower: {0}, Upper: {1}".format(lower, upper))

print("\nArbitrary nested tuples. (a,(b,(c,d))) = (4,(3,(2,1)))")
(a,(b,(c,d))) = (4,(3,(2,1)))
print("\na: {0}\nb: {1}\nc: {2}\nd: {3}".format(a, b, c, d))

print("\nSwaping variables: a, b = b, a")
a = "jelly"
b = "bean"
print("\na: {0}\nb: {1}".format(a, b))
a, b = b, a
print("\na: {0}\nb: {1}".format(a, b))

print("\nConvert list to tuple. t = tuple(myList) ")
myList = [561, 234, 345, 897]
t = tuple(myList)
print("\nList: ")
print(myList)
print("\nTuple: ")
print(t)

print("\n Is 234 in Tuple?: [{0}] (234 in t)".format(234 in t))

