my_set={1,2,2,3,4,4,4}
print("Set: ",my_set)
my_set.add(5)
print("Updated set: ",my_set)
set1=my_set
set2={2,4,4,6}
print('\nSet1: ',set1)
print('Set2: ',set2)
print('Difference: ')
print(set1.difference(set2))
print('Symmetric Difference: ')
print(set1.symmetric_difference(set2))
setx={'green','blue'}
sety={'blue','yellow'}
print('Original elements of set')
print(setx)
print(sety)
print('\nUnion of two said sets: ')
setz=setx.union(sety)
print(setz)
print('\nIntersection of two said sets')
setz=setx.intersection(sety)
print(setz)