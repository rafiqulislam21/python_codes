#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered and unindexed. No duplicate members.
#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(len(thislist))
thislist.append("orange")
thislist.insert(1, "orange")
thislist.remove("banana")
thislist.pop()

thislist.reverse()
thislist.sort()

del thislist[0]
print(thislist)
for x in thislist:
  print(x)

thislist.clear()
mylist = thislist.copy()
del thislist



list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
list1.extend(list2)
print(list3)

#tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
x = thisdict["model"]
x = thisdict.get("model")
for x in thisdict.values():
  print(x)

for x, y in thisdict.items():
  print(x, y)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
