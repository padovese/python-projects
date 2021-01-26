#list: ordered, immutable, allow duplicate elements
import sys

myTuple = ("Bruno", 29, "Padovese")
print(myTuple)
print(type(myTuple))

item = myTuple[0]
print(item)

for i in myTuple:
    print(i)

if "Padovese" in myTuple:
    print("yes")
else:
    print("no")

print(len(myTuple))

myList = list(myTuple)
print(myList)
print(tuple(myList))

#tuples are lighter than lists thus more performatic
print(sys.getsizeof(myTuple), "bytes") #72
print(sys.getsizeof(myList), "bytes") #112