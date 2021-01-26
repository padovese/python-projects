#dictionary: key-value pairs, unordered, mutable
myDict = {"name": "Bruno", "age": 29, "surname": "Padovese"}
print(myDict)

item = myDict["surname"]
print(item)

#add item
myDict["email"] = "padova@gmail.com"
print(myDict)

#delete item
del myDict["email"]
print(myDict)

myDict.pop("name")
print(myDict)

if "name" in myDict:
    print("yes")
else:
    print("no")

try:
    print(myDict["name"])
except:
    print("name not found")


#loop
for key in myDict:
    print(key)

for val in myDict.values():
    print(val)

for k, v in myDict.items():
    print(k, v)

#copy a dict
myDict2 = myDict.copy()
myDict3 = dict(myDict)

#merge two dict
myDict4 = dict(name="Bruno", age=30)
myDict.update(myDict4)
print(myDict)