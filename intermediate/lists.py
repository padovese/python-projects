#list: ordered, mutable, allow duplicate elements

#instantiate a list
myList = ["banana", "apple", "watermelon"]
print(myList)

#empty list
myList2 = list()
print(myList2)

myList3 = [5, True, "apple", "apple"]
print(myList3)

#loop the list
for i in myList3:
    print(i)

#check if an element is in the list
if "apple" in myList3:
    print("yes")
else:
    print("no")

#size
print(len(myList3))

#add element
myList3.append("lemon")
print(myList3)

#remove last element
item = myList3.pop()
print(item)
print(myList3)

#remove specific element
myList3.remove("apple")
print(myList3)

#reverse the elements order
myList3.reverse()
print(myList3)

#sort, only work with strings or numbers
myList.sort()
print(myList)

#range
myList4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
specificRange = myList4[1:4]
print(specificRange)

rangeUntilTheLastElement = myList4[2:]
print(rangeUntilTheLastElement)

rangeFromTheFirstElement = myList4[:5]
print(rangeFromTheFirstElement)

rangeHoppingByTwo = myList4[::2]
print(rangeHoppingByTwo)

rangeHoppingByMinusTwo = myList4[::-2]
print(rangeHoppingByMinusTwo) #reverse the list

#copy elements from a list
myCopy = myList4.copy()
myCopy2 = list(myList4)
myCopy3 = myList4[:]

#process data of a list
processedList = [i%2 == 0 for i in myList4]
processedList2 = [i*i for i in myList4]


print(processedList)
print(processedList2)