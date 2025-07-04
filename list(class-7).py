lst=["Mango","Strawberry","Banana","Apple","Litchi","Grapes"]
print("Length of the list: ",len(lst))
print("\nList's first & last item: \n",lst[0],"\n",lst[-1])
lst.append("Guava")
print("\nUpdated list: ",lst)
lst.remove("Litchi")
print("\nUpdated list: ",lst)
lst.pop(2)
print("\nUpdated list: ",lst)
lst.sort()
print("\nSorted list: ",lst)
lst.reverse()
print("\nUpdated list: ",lst)
print("\nMultiplication of list: ",lst*2)
lst=lst[:4]
print("\nSliced list: ",lst)
lst.clear
print("\nUpdated list: ",lst)