myneighbours=[16,17,18]
neighbours=myneighbours #copy of the list
print("Initial list is :",myneighbours)
myneighbours.append(19)
print("List after appending is :",myneighbours)
myneighbours.insert(0,15)
print("List after inserting is  :",myneighbours)
myneighbours.pop(0)
print("List after popping a specific element is  :",myneighbours)
myneighbours.pop()
print("List after popping is  :",myneighbours)
myneighbours.remove(17)
print("List after removing an element is  :",myneighbours)
myneighbours.reverse()
print("List after reversing the list is :",myneighbours)
myneighbours.sort()
print("List after sorting the list is :",myneighbours)
neighbours=myneighbours
myneighbours.clear()
print("List after clearing",myneighbours)
del myneighbours

