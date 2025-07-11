my_tuple=(1,2,3,4,'Computer','Coding')
print(my_tuple)
#Converting tuple to list 1st way
my_list=[my_tuple[0],my_tuple[1],my_tuple[2],my_tuple[3],my_tuple[4],my_tuple[5]]
print(my_list)
#Converting tuple to list 2nd way
for i in (my_tuple):
    s_list=[i]
    print(s_list)